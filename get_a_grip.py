#Get a grip backend code

def code_executor():#->  code_executor is our main function and this is where we call all of our ot
    arm.home()
    time.sleep(2)
    while len(ids) < 6:
        global container_ID
        container_ID = random.randint(1,6) #> Here we assign a random value to the variable container_ID
        while container_ID in ids: #-->While loop that makes sure container being spawned is unique.
            container_ID = random.randint(1, 6)
        ids.append(container_ID) #-> Adds container ID of the spawned container in the list "ids"


        arm.spawn_cage (container_ID)
        time.sleep(2)
        print("The container ID is: ", container_ID)
        identify_bin()
        time.sleep(3)
        move_to_pickup_location()
        time.sleep(3)
        close_control_gripper()
        time.sleep(3)
        move_end_effector()
        time.sleep(4)
        open_bin (container_ID)
        time.sleep(4)
        open_control_gripper()
        time.sleep(3)
        close_bin (container_ID)
        arm.home()
        time.sleep(2)

        print("These containers have been deposited", ids)

def identify_bin():
    
    if container_ID == 1:
        print("The container is red in colour and small. Place in red bin overhead")
        
    elif container_ID == 2:
        print("The container is green in colour and small. Place in green bin overhead")
        
    elif container_ID == 3:
        print("The container is blue in colour and small. Place in blue bin overhead")
        
    elif container_ID == 4:
        print("The container is red in colour and large. Open red bin drawer and place in it")
        
    elif container_ID == 5:
        print("The container is green in colour and large. Open green bin drawer and place in it")
        
    elif container_ID == 6:
        print("The container is blue in colour and large. Open blue bin drawer and place in it")


def move_to_pickup_location():
    
    if arm.emg_left()> threshold and arm.emg_right()== 0.0:
        arm.move_arm(container_pickup_location[0], container_pickup_location [1], container_pickup_location [2])

def close_control_gripper():

    if arm.emg_left() > threshold and arm. emg_right()> threshold:
        arm.control_gripper (30)

    

    











