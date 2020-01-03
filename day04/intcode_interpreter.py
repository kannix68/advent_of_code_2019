class IntcodeInterpreter:
  INITIALIZED = 0
  RUNNING = 1
  HALTED = 99

  def __init__(self, mem):
    self.mem = mem.copy()
    #self.mem0 = mem.copy()
    self.ptr = 0  # instruction pointer
    self.ctr = 0  # instruction counter
    self.state = self.INITIALIZED
    print(f"initialized {self}")

  def __repr__(self):
    return "IntcodeInterpreter"

  def __str__(self):
    return f"IntcodeInterpreter ptr={self.ptr}, ctr={self.ctr}, state={self.state} mem={self.mem}"

  def step_program(self) -> None:
    """Interpret the program given in the puzzle (1 step). list in, list out."""
    mem = self.mem
    ptr = self.ptr
    #print(f"to-step {self}")
    opcode = mem[ptr]
    if opcode == 1:
      op1 = mem[ptr+1]
      op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = mem[op1] + mem[op2]
      self.ptr += 4
    elif opcode == 2:
      op1 = mem[ptr+1]
      op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = mem[op1] * mem[op2]
      self.ptr += 4
    elif opcode == 99:
      self.state = self.HALTED
    else:
      raise(RuntimeError(f"illegal opcode {opcode}")) 
    self.ctr += 1
    #print(f"stepped! {self}")

  def interpret_program(self) -> None:
    """Interpret the program given in the puzzle (all steps until prg-exit). list in, list out."""
    self.state = self.RUNNING
    while self.state != self.HALTED:
      self.step_program()
    print(f"interpreted halted! {self}")
