def get_greatest_difference(nums):
  min=0
  max=0

  for num in nums:
    if num > max:
      max=num

    if num < min:
      min=num


  print max- min


print get_greatest_difference([10,40,100,30])