is_duplicate:
  push rbp
  mov rbp, rsp
  mov QWORD PTR [rbp-24], rdi
  mov QWORD PTR [rbp-32], rsi
  mov rax, QWORD PTR [rbp-24]
  mov QWORD PTR [rbp-8], rax
  jmp .L2
.L7:
  mov rax, QWORD PTR [rbp-8]
  add rax, 1
  mov QWORD PTR [rbp-16], rax
  jmp .L3
.L6:
  mov rax, QWORD PTR [rbp-8]
  movzx edx, BYTE PTR [rax]
  mov rax, QWORD PTR [rbp-16]
  movzx eax, BYTE PTR [rax]
  cmp dl, al
  jne .L4
  mov eax, 1
  jmp .L5
.L4:
  add QWORD PTR [rbp-16], 1
.L3:
  mov rax, QWORD PTR [rbp-16]
  cmp rax, QWORD PTR [rbp-32]
  jb .L6
  add QWORD PTR [rbp-8], 1
.L2:
  mov rax, QWORD PTR [rbp-8]
  cmp rax, QWORD PTR [rbp-32]
  jb .L7
  mov eax, 0
.L5:
  pop rbp
  ret
.LC0:
  .string "%d\n"
main:
  push rbp
  mov rbp, rsp
  sub rsp, 48
  mov DWORD PTR [rbp-36], edi
  mov QWORD PTR [rbp-48], rsi
  cmp DWORD PTR [rbp-36], 2
  jg .L9
  mov edi, 2
  call exit
.L9:
  mov rax, QWORD PTR [rbp-48]
  add rax, 8
  mov rax, QWORD PTR [rax]
  mov edx, 10
  mov esi, 0
  mov rdi, rax
  call strtol
  mov DWORD PTR [rbp-8], eax
  mov rax, QWORD PTR [rbp-48]
  mov rax, QWORD PTR [rax+16]
  mov QWORD PTR [rbp-16], rax
  mov rax, QWORD PTR [rbp-16]
  mov rdi, rax
  call strlen
  mov QWORD PTR [rbp-24], rax
  mov DWORD PTR [rbp-4], 0
  jmp .L10
.L13:
  mov eax, DWORD PTR [rbp-4]
  movsx rdx, eax
  mov eax, DWORD PTR [rbp-8]
  cdqe
  add rdx, rax
  mov rax, QWORD PTR [rbp-16]
  add rdx, rax
  mov eax, DWORD PTR [rbp-4]
  movsx rcx, eax
  mov rax, QWORD PTR [rbp-16]
  add rax, rcx
  mov rsi, rdx
  mov rdi, rax
  call is_duplicate
  test eax, eax
  je .L15
  add DWORD PTR [rbp-4], 1
.L10:
  mov eax, DWORD PTR [rbp-4]
  movsx rcx, eax
  mov eax, DWORD PTR [rbp-8]
  cdqe
  mov rdx, QWORD PTR [rbp-24]
  sub rdx, rax
  cmp rcx, rdx
  jb .L13
  jmp .L12
.L15:
  nop
.L12:
  mov edx, DWORD PTR [rbp-4]
  mov eax, DWORD PTR [rbp-8]
  add eax, edx
  mov esi, eax
  mov edi, OFFSET FLAT:.LC0
  mov eax, 0
  call printf
  mov eax, 0
  leave
  ret