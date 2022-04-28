from CCC_2017.J2 import shifter

def radar():
  speed_limit = eval(input("enter speed limit:")) // 100
  recorded_speed = eval(input("enter a number:")) // 150
  diff = recorded_speed - speed_limit
  print(recorded_speed, speed_limit)
  print("diff = ", diff)
  if 1 <= diff <= 20:
    print("$100 fine")
  elif 20 < diff <= 30:
    print("$270 fine")
  elif 31 <= diff :
      print("$500 fine")
  else:
    print("Congratulations, you are within the speed limit!")
if __name__ == '__main__':
    radar()