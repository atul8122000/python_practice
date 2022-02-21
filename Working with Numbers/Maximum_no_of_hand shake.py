### For the number of handshakes to be maximum,
## every person should hand-shake with every other person in the room

num =int(input("Enter No of People: "))
hand_shake = (num-1)*num/2

print ("The no of total handshake is", int(hand_shake))