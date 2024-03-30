Checksum Error Detection Calculation Program

This Python program is designed for checksum error detection. It operates in two phases: the sender side and the receiver side. Here's a breakdown of its functionality:
Sender Side:

    Input: The program takes the number of frames and the frames themselves as input.
    Calculation: It computes the checksum by summing up the frames step by step and displays the process.
    Output: Finally, it provides the checksum value to be sent by the sender.

Receiver Side:

    Input: Assuming all frames are received, the program takes the received frames as input.
    Calculation: It calculates the checksum step by step, similar to the sender side.
    Output: The receiver computes the checksum and compares it with the checksum sent by the sender.
    Verification: Based on the comparison, it determines whether the received data is erroneous or not.

How to Use:

    Clone this repository to your local machine.
    Run the Python program, providing the necessary inputs.
    Follow the step-by-step instructions to understand the checksum calculation process.
    Check the final result to determine if the received data is erroneous or not.

Example Usage:

bash
$ python3 checksum.py

Note:

    This program assumes that all frames are received intact.
    Ensure to provide the correct inputs as per the program's requirements.

Feel free to contribute to or fork this repository for further enhancements!
