class IntcodeInterpreter:
  STATE_INITIALIZED = 0
  STATE_RUNNING = 1
  STATE_HALTED = 99
  
  MODE_POSITION = 0
  MODE_IMMEDIATE = 1

  def __init__(self, mem):
    self.mem = mem.copy()
    #self.mem0 = mem.copy()
    self.ptr = 0  # instruction pointer
    self.ctr = 0  # instruction counter
    self.state = self.STATE_INITIALIZED
    self.pseudo_stdin = []
    self.pseudo_stdout = []
    print(f"initialized {self}")

  def __repr__(self):
    return "IntcodeInterpreter"

  def __str__(self):
    return f"IntcodeInterpreter ptr={self.ptr}, ctr={self.ctr}, state={self.state} mem-len={len(self.mem)}"

  def step_program(self) -> None:
    """Interpret the program given in the puzzle (1 step). list in, list out."""
    mem = self.mem
    ptr = self.ptr
    print(f"  to-step {self}")
    instruction = mem[ptr]
    opcode = instruction % 100  # 1 to 2 digits
    p1_mode = (instruction // 100) % 10  # single digit
    p2_mode = (instruction // 1000) % 10  # single digit
    p3_mode = (instruction // 10000) % 10  # single digit
    print(f"  instruction={instruction}: opcode={opcode}, mmodes={[p1_mode, p2_mode, p3_mode]}")
    if opcode == 1:  # ADD
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = op1 + op2
      self.ptr += 4
    elif opcode == 2:  # MUL
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = op1 * op2
      self.ptr += 4
    elif opcode == 3:  # IN
      # take an input value "from pseudo-stdin" and store it
      # always uses implicit MODE_POSITION
      op = self.fetch_int_stdin()
      trg = mem[ptr+1]
      mem[trg] = op
      self.ptr += 2
    elif opcode == 4:  # OUT
      # output a value to "pseudo-stdout"
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      self.pseudo_stdout.append(op1)
      print(f"OUT>> {op1}")
      self.ptr += 2
    elif opcode == 5:  # JNZ jump-if-true
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if op1 != 0:
        if p2_mode == self.MODE_POSITION:
          op2 = mem[ mem[ptr+2] ]
        elif p2_mode == self.MODE_IMMEDIATE:
          op2 = mem[ptr+2]
        self.ptr = op2
      else:
        #"it does nothing"
        self.ptr += 3  #"it does nothing"
    elif opcode == 6:  # JZ jump-if-false
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if op1 == 0:
        if p2_mode == self.MODE_POSITION:
          op2 = mem[ mem[ptr+2] ]
        elif p2_mode == self.MODE_IMMEDIATE:
          op2 = mem[ptr+2]
        self.ptr = op2
      else:
        self.ptr += 3  #"it does nothing"
    elif opcode == 7:  # LT less-than
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      trg = mem[ptr+3]
      if op1 < op2:
        mem[trg] = 1
      else:
        mem[trg] = 0
      self.ptr += 4
    elif opcode == 8:  # EQ equals
      if p1_mode == self.MODE_POSITION:
        op1 = mem[ mem[ptr+1] ]
      elif p1_mode == self.MODE_IMMEDIATE:
        op1 = mem[ptr+1]
      if p2_mode == self.MODE_POSITION:
        op2 = mem[ mem[ptr+2] ]
      elif p2_mode == self.MODE_IMMEDIATE:
        op2 = mem[ptr+2]
      trg = mem[ptr+3]
      if op1 == op2:
        mem[trg] = 1
      else:
        mem[trg] = 0
      self.ptr += 4
    elif opcode == 99:  # HALT (Halt and Catch Fire!!!)
      self.state = self.STATE_HALTED
    else:
      raise(RuntimeError(f"illegal opcode {opcode}")) 
    self.ctr += 1
    print(f"stepped! {self}")

  def interpret_program(self) -> None:
    """Interpret the program given in the puzzle (all steps until prg-exit). list in, list out."""
    self.state = self.STATE_RUNNING
    while self.state != self.STATE_HALTED:
      self.step_program()
    print(f"interpreted halted! {self}")

  def store_int_stdin(self, i: int) -> None:
    self.pseudo_stdin.append(i)
  
  def fetch_int_stdin(self) -> int:
    i = self.pseudo_stdin.pop(0)
    return i