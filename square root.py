def is_perfect_square(num):
   square_root=num**0.5
   return square_root==int(square_root)

number=int(input("Enter a number:"))

if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")