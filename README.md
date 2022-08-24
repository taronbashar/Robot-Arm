# Robot-Arm
Mechanical arm powered and controlled using a raspberry pi 3, used for color recognition of game pieces for vertical stacking in a specific order. An external camera attached to the raspberry pi, is used to detect the different colors of the vertically stacked game pieces, which are then stored in variables. The user then inputs a different color sequence for stacking the game pieces in the target area and the robot arm begins removing stacked pieces from the repository accordingly. If the first piece moved is not the first piece to be placed in the target area, the game piece is temporarily placed in the staging area before it is later moved to the target area in the correct seqeunce.

Here is a CAD model of the base plate with the three different areas:

<img width="500" alt="Screen Shot 2021-04-07 at 3 19 12 PM" src="https://user-images.githubusercontent.com/111838744/186303891-691afa1d-eba7-4d1a-a6de-2623f1c12e1b.png"> <img width="500" alt="Screen Shot 2021-04-07 at 3 19 07 PM" src="https://user-images.githubusercontent.com/111838744/186303897-d34a3c5c-2a5b-4351-8116-77aaea1a775b.png">

Before running the script, the robot arm was manually calibrated for the placement of the game pieces at different height levels:
<img width="480" alt="Screen Shot 2021-04-28 at 8 22 42 PM" src="https://user-images.githubusercontent.com/111838744/186304163-1464e416-a1f2-4e50-899a-63e5f55a935f.png">

Here, is a demo of the robot arm reversing the stacking order using two game pieces:

https://user-images.githubusercontent.com/111838744/186304264-2f566284-fa7b-4723-aaa7-aa1d9d99ef8b.MOV


