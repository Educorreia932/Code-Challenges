use std::io::{self, Read, Write};

fn main() {
    let code = ">,<>>,>,<[->->+<><<]+->>[-<<+>>]<+-><><<<[-+->-<+-<+>]<[->+<]><>>>>>><>++->>+->>>>>+[>><>>>[-]<[-<>-+]<<>[-+-]-++-+-<[-]<><<>[+---+]<><<<<+-<<<<>-+<><<<><+-<<[->>>>>>>+>>>>>-+>+<<<><<<><<<<<<<<<]>[->>>>><><>><>>+>>>>>>+<<<<<><<<<<+-<<<<]>[->>>>>>><>+>>>>-+><>>+<<<<<<+-<<<<><<<<-+><]>>-++-+>+-+[<-]<[->><>++-<<<]>>>>[-<<<+--+<<<<+>><>>>>>>]>[-<<-+<<<<<+<>>+->>>>>>]>[-<<<<><<<><<+>>>>>>>]>>>>>><>>+[-<<<<+--+<><+-<<<<<<[->>+>>+<<<<]+->[->>+>>+-+<<<<]>[-<<+>>]>[-<<+>>]+[[<>-]-++>[<-]<+-[+--><>><>-<<<]>>-+->>>+>[<-]<+-[->+>[-<-]<[>>[-<<-+->]-<<[->><->+->-+-<<<<]]<]>>-<<<<<+>[><<-]<[>+->[-+<<->]<<[<]]>-+-]>>>>><>>>><>+]-<<<>+-<<<>+>-++[<-]<[-+>>+[<<<>->-+]<<[>>>+[<-+<<->>]<<<[<]]]>-]>>>>[-]<<<<<<<-+<><<<<<<<[-]>>+>+[<-]<[->>+<><<<]>+>[<-]<[>>[<<->]<<[<]]>-[+>>>>>>><++-+++++++++<<<<<<+>+-[<<>-]<[>>[<<->]<<[<]]>-[++>[<-]<[->>-<<<]>>->>+>>+>-[<-]<[<<[->>>+<<><<]+->>>>>+>+[<><-]<><[->>+<<<]<<-<]<<<<+>[<-]<[>>[<<->]<<[<]]>-]>>++++++++[->++++++<]>[-<<<<+>>>>]>>>>>+><>-+[<-]<[>>[<<->]<<[<]]>-[++>[<-]<[->>-<<<]>>-<<<<<<<<+>+[<-]<[->>+<<<]>>>>>>>>+>[<-]<[>>[<<->]<<[<]]>-]<<[-]<<<<<+>[<-]<[>>[<<->]<<[<]]>-]<<[.<]!";
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let n_lines: i32 = buffer.trim().parse().unwrap();

    // let mut vm = BFVM::new(code);
    // vm.run();
    
    for _ in 0..n_lines {
        BFVM::new(code).run();
        println!();
    }
}

#[derive(Eq, PartialEq)]
enum Direction {
    Forward,
    Backward,
}

enum OpCode {
    Increment(u8),
    Decrement(u8),
    MoveLeft(usize),
    MoveRight(usize),
    Zero,
    Read,
    Write,
    Jump {
        destination: usize,
        direction: Direction,
    },
}

fn compile(code: &Vec<char>) -> Vec<OpCode> {
    let mut res = Vec::new();
    let mut index = 0;
    let mut jumps: Vec<usize> = Vec::new();

    while index < code.len() {
        match code[index] {
            '<' | '>' | '+' | '-' => {
                let hit = code[index];
                let mut len = 1;
                while index + len < code.len() && code[index + len] == hit {
                    len += 1;
                }

                let opcode = match code[index] {
                    '<' => OpCode::MoveLeft(len),
                    '>' => OpCode::MoveRight(len),
                    '+' => OpCode::Increment(len as u8),
                    '-' => OpCode::Decrement(len as u8),
                    _ => panic!(),
                };

                res.push(opcode);
                index += len;
            }
            '.' => {
                res.push(OpCode::Write);
                index += 1;
            }
            ',' => {
                res.push(OpCode::Read);
                index += 1;
            }

            '[' => {
                if index + 2 < code.len() && code[index + 1] == '-' && code[index + 2] == ']' {
                    // [-]
                    res.push(OpCode::Zero);
                    index += 3;
                } else {
                    res.push(OpCode::Jump {
                        direction: Direction::Forward,
                        destination: 0,
                    });
                    index += 1;

                    jumps.push(res.len() - 1);
                }
            }
            ']' => {
                let dest = jumps.pop().unwrap();

                if !matches!(&res[dest], OpCode::Jump{destination : _, direction : _}) {
                    panic!();
                }

                res[dest] = OpCode::Jump {
                    direction: Direction::Forward,
                    destination: res.len(),
                };

                res.push(OpCode::Jump {
                    direction: Direction::Backward,
                    destination: dest,
                });
                index += 1;
            }
            _ => index += 1,
        }
    }
    res
}

struct BFVM {
    memory: [u8; 300000],
    mem_pointer: usize,

    code: Vec<OpCode>,
    code_pointer: usize,
}

impl BFVM {
    fn new(code: &str) -> Self {
        Self {
            memory: [0; 300000],
            mem_pointer: 0,
            code: compile(&code.chars().collect()),
            code_pointer: 0,
        }
    }

    fn run(&mut self) {
        self.mem_pointer = 0;
        self.code_pointer = 0;
        for i in self.memory.iter_mut() {
            *i = 0;
        }

        while self.code_pointer < self.code.len() {
            match &self.code[self.code_pointer] {
                OpCode::Increment(i) => {
                    self.memory[self.mem_pointer] =
                        self.memory[self.mem_pointer].overflowing_add(i.clone()).0
                }
                OpCode::Decrement(i) => {
                    self.memory[self.mem_pointer] =
                        self.memory[self.mem_pointer].overflowing_sub(i.clone()).0
                }
                OpCode::MoveLeft(i) => self.mem_pointer -= i,
                OpCode::MoveRight(i) => self.mem_pointer += i,
                OpCode::Zero => self.memory[self.mem_pointer] = 0,
                OpCode::Read => self.read_input(),
                OpCode::Write => print!("{}", self.memory[self.mem_pointer] as char),
                _ => (),
            }

            match &self.code[self.code_pointer] {
                OpCode::Jump {
                    destination,
                    direction,
                } => {
                    let zero = self.memory[self.mem_pointer] == 0;
                    if (direction == &Direction::Forward && zero)
                        || direction == &Direction::Backward && !zero
                    {
                        self.code_pointer = destination.clone();
                    } else {
                        self.code_pointer += 1;
                    }
                }
                _ => self.code_pointer += 1,
            }
        }
    }

    fn read_input(&mut self) {
        let input: Option<u8> = std::io::stdin()
            .bytes()
            .filter(|c| 33 <= *c.as_ref().unwrap() && *c.as_ref().unwrap() <= 126)
            .next()
            .and_then(|result| result.ok());

        self.memory[self.mem_pointer] = input.unwrap();
    }
}
