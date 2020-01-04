##
# Advent of code 2019, IntCode Interpreter.
# This class (python3.7 jupyter notebook) by kannix68, @ 2020-01-04.
#
# History:
# 2020-01-04  ok for day 9 (adressing relative-mode, growable memory-list)
# ...
# 2019-12-30  started, ok for day 2

# see [Automatically growing lists in Python - Stack Overflow](https://stackoverflow.com/questions/4544630/automatically-growing-lists-in-python)
class GrowableList(list):
  def __init__(self, init_value=None):
    print(f"initialize GrowableList with init_value={init_value}")
    self.init_value = init_value
    # super call, see: [class - How to invoke the super constructor in Python? - Stack Overflow](https://stackoverflow.com/questions/2399307/how-to-invoke-the-super-constructor-in-python)
    super(GrowableList, self).__init__()

  def __getitem__(self, index):
    #print(f"GrowableList.__getitem__(self, {index}) called")
    if index >= len(self):
      self.__setitem__(index, 0)
    return list.__getitem__(self, index)

  def __setitem__(self, index, value):
    #print(f"GrowableList.__setitem__(self, {index}, {value}) called")
    if index >= len(self):
      extend_size = index + 1 - len(self)
      print(f"GrowableList: extend list by {extend_size} to cope with index={index}")
      self.extend([self.init_value]*(extend_size))
    list.__setitem__(self, index, value)


class IntcodeInterpreter:
  """A class implementation of Advent of Code 2019's recurring IntCode computer."""

  STATE_INITIALIZED = 0
  STATE_RUNNING = 1
  STATE_PAUSED = 88
  STATE_HALTED = 99
  
  MODE_POSITION = 0
  MODE_IMMEDIATE = 1
  MODE_RELATIVE = 2

  def __init__(self, mem, mem_growable=False):
    self.mem_growable = mem_growable
    if not mem_growable:
      self.mem = mem.copy()
    else:
      gmem = GrowableList(init_value=0)
      for i in mem:
        gmem.append(i)
      self.mem = gmem
      print(f"initialized growable memory len={len(gmem)}")
    #self.mem0 = mem.copy()
    self.ptr = 0  # instruction pointer
    self.ctr = 0  # instruction counter
    self.state = IntcodeInterpreter.STATE_INITIALIZED
    self.pseudo_stdin = []
    self.pseudo_stdout = []
    self.relative_base = 0
    #print(f"initialized {self}")

  def __repr__(self):
    return "IntcodeInterpreter"

  def __str__(self):
    return f"IntcodeInterpreter ptr={self.ptr}, ctr={self.ctr}, state={self.state}, rel-base={self.relative_base}, mem-len={len(self.mem)}"

  def step_program(self) -> None:
    """Interpret the program given in the puzzle (1 step). list in, list out."""
    mem = self.mem
    ptr = self.ptr
    rbs = self.relative_base
    #print(f"  to-step {self}")
    instruction = mem[ptr]
    opcode = instruction % 100  # 1 to 2 digits
    p1_mode = (instruction // 100) % 10  # single digit
    p2_mode = (instruction // 1000) % 10  # single digit
    p3_mode = (instruction // 10000) % 10  # single digit
    #print(f"  instruction={instruction}: opcode={opcode}, mmodes={[p1_mode, p2_mode, p3_mode]}")
    if opcode == 1:  # ADD
      # 3 params: 2 mode-params, 1 write-target
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      elif p2_mode == self.MODE_RELATIVE:
        op2 = mem[ mem[ptr+2] + rbs ]
      if p3_mode == self.MODE_POSITION:
        trg = mem[ptr+3]
      elif p3_mode == self.MODE_IMMEDIATE:
        raise(RuntimeError(f"MODE_IMMEDIATE not defined for opcode=1=ADD")) 
      elif p3_mode == self.MODE_RELATIVE:
        trg = mem[ptr+3] + rbs
      mem[trg] = op1 + op2
      self.ptr += 4
    elif opcode == 2:  # MUL
      # 3 params: 2 mode-params, 1 write-target
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      elif p2_mode == self.MODE_RELATIVE:
        op2 = mem[ mem[ptr+2] + rbs ]
      if p3_mode == self.MODE_POSITION:
        trg = mem[ptr+3]
      elif p3_mode == self.MODE_IMMEDIATE:
        raise(RuntimeError(f"MODE_IMMEDIATE not defined for opcode=2=MUL")) 
      elif p3_mode == self.MODE_RELATIVE:
        trg = mem[ptr+3] + rbs
      mem[trg] = op1 * op2
      self.ptr += 4
    elif opcode == 3:  # IN
      # take an input value "from pseudo-stdin" and store it
      if self.pause_on_input and len(self.pseudo_stdin)==0:
        self.state = self.STATE_PAUSED
        return
      elif self.pause_on_input and len(self.pseudo_stdin)>0:
        op_read_in = self.fetch_int_stdin()
      else:
        op_read_in = self.fetch_int_stdin()
        trg = -1
        if p1_mode == self.MODE_POSITION:
          trg = mem[ptr+1]
        elif p1_mode == self.MODE_IMMEDIATE:
          raise(RuntimeError(f"MODE_IMMEDIATE not defined for opcode=3=IN")) 
        elif p1_mode == self.MODE_RELATIVE:
          trg = mem[ptr+1] + rbs
        mem[trg] = op_read_in
        self.ptr += 2
    elif opcode == 4:  # OUT
      # output a value to "pseudo-stdout"
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      self.pseudo_stdout.append(op1)
      if self.pause_on_output:
        self.state = self.STATE_PAUSED
      #print(f"OUT>> {op1}")
      self.ptr += 2
    elif opcode == 5:  # JNZ jump-if-true
      # 2 params: 2 mode-params
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if op1 != 0:
        if p2_mode == self.MODE_POSITION:
          op2 = mem[ mem[ptr+2] ]
        elif p2_mode == self.MODE_IMMEDIATE:
          op2 = mem[ptr+2]
        elif p2_mode == self.MODE_RELATIVE:
          op2 = mem[ mem[ptr+2] + rbs ]
        self.ptr = op2
      else:
        #"it does nothing"
        self.ptr += 3  #"it does nothing"
    elif opcode == 6:  # JZ jump-if-false
      # 2 params: 2 mode-params
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if op1 == 0:
        if p2_mode == self.MODE_POSITION:
          op2 = mem[ mem[ptr+2] ]
        elif p2_mode == self.MODE_IMMEDIATE:
          op2 = mem[ptr+2]
        elif p2_mode == self.MODE_RELATIVE:
          op2 = mem[ mem[ptr+2] + rbs ]
        self.ptr = op2
      else:
        self.ptr += 3  #"it does nothing"
    elif opcode == 7:  # LT less-than
      # 3 params: 2 mode-params, 1 write-target
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      elif p2_mode == self.MODE_RELATIVE:
        op2 = mem[ mem[ptr+2] + rbs ]
      if p3_mode == self.MODE_POSITION:
        trg = mem[ptr+3]
      elif p3_mode == self.MODE_IMMEDIATE:
        raise(RuntimeError(f"MODE_IMMEDIATE not defined for opcode=7=LT")) 
      elif p3_mode == self.MODE_RELATIVE:
        trg = mem[ptr+3] + rbs
      if op1 < op2:
        mem[trg] = 1
      else:
        mem[trg] = 0
      self.ptr += 4
    elif opcode == 8:  # EQ equals
      # 3 params: 2 mode-params, 1 write-target
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      elif p2_mode == self.MODE_RELATIVE:
        op2 = mem[ mem[ptr+2] + rbs ]
      if p3_mode == self.MODE_POSITION:
        trg = mem[ptr+3]
      elif p3_mode == self.MODE_IMMEDIATE:
        raise(RuntimeError(f"MODE_IMMEDIATE not defined for opcode=8=EQ")) 
      elif p3_mode == self.MODE_RELATIVE:
        trg = mem[ptr+3] + rbs
      if op1 == op2:
        mem[trg] = 1
      else:
        mem[trg] = 0
      self.ptr += 4
    elif opcode == 9:  # adjust-relative-base (for MODE_RELATIVE usage)
      # 1 param: 1 mode-param
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      elif p1_mode == self.MODE_RELATIVE:
        op1 = mem[ mem[ptr+1] + rbs ]
      self.relative_base += op1
      self.ptr += 2
    elif opcode == 99:  # HALT (Halt and Catch Fire!!!)
      # 0 params
      self.state = self.STATE_HALTED
    else:
      raise(RuntimeError(f"illegal opcode {opcode}")) 
    self.ctr += 1
    #print(f"stepped! {self}")

  def interpret_program(self, pause_on_output = False, pause_on_input = False) -> None:
    """Interpret the program given in the puzzle (all steps until prg-exit). list in, list out."""
    self.state = self.STATE_RUNNING
    self.pause_on_output = pause_on_output
    self.pause_on_input = pause_on_input
    while self.state != self.STATE_HALTED and self.state != self.STATE_PAUSED:
      self.step_program()
    #print(f"interpreted halted! {self}")

  def store_int_stdin(self, i: int) -> None:
    """Store an input value (programmatically)."""
    self.pseudo_stdin.append(i)
  
  def fetch_int_stdin(self) -> int:
    """Internal. Fetch an input value stored previously. It will be removed from pseaudo_stdin"""
    i = self.pseudo_stdin.pop(0)
    return i

  def fetch_int_stdout(self) -> int:
    """Fetch an output value produced previously. It will be removed from pseaudo_stdout"""
    i = self.pseudo_stdout.pop(0)
    return i

  def has_output(self) -> bool:
    return len(self.pseudo_stdout) > 0

  def waits_for_input(self) -> bool:
    return self.STATE_PAUSED and len(self.pseudo_stdin) == 0 and not self.has_output()

class IntcodeSimulator(IntcodeInterpreter):
  def interpret_program(self, pause_on_output = False, pause_on_input = False) -> None:
    return

  def next_pause_for_input(self):
    self.state = IntcodeInterpreter.STATE_PAUSED
    self.pseudo_stdin = []
    self.pseudo_stdout = []

  def next_consume_input(self):
    self.fetch_int_stdin()

  def next_output(self, i):
    self.pseudo_stdout.append(i)


