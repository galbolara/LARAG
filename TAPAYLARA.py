while True:
    otp = input("Enter OTP: ")
    found = False

    if otp == "123456":
        found = True

    if found:
        print("OTP accepted!")
    else:
        print("Incorrect OTP!")

    again = input("Try again? (Y/N): ")

    if again.upper() == "Y":
        print("Restarting...")

    elif again.upper() == "N":
        print("ALL GOODS")
        break

    else:
        print("INVALID OPTION")
        break