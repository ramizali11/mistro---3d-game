# mistro-3d game
I Made A Game With Python Using The Module Ursina To Understand And Practice The Python More From The Difficulties Like Player Healthbar Managemet, Player Demage Menagement And More, It Give Me Much Difficulties To Solve And I Solved Numbers Of Difficulties But Still Some Function Are Remain That I Am Not Able To Make In The Game 

# Features
1. Healthbar: I Created HealthBar To Observe The Player Health If Player Health == 0 Player Will Die.

3. Gun: I Add A 3D Gun To Shoot The Enemy Or We Can Say The Zombie, I Took The 3D Model From sketchfab.com
4. Enemy: I Also Add The Enemy As A Zombie, When The Player Come Colse To Enemy The Player Take Demage
5. Enemy Demage: When Player Shoot Enemy Take Demage
6. Fall Demage: I Had NO Idea How To Manage The Fall Demage But I Did It (Explain It Later)
7. Dead When Fall Out OF The Land: So My Gmae have The Island Where Player Lie But If Player Fall Out Of The Land Player will Die : if player.y = -30 -> dead()
8. Dead UI: If player Die HE/She Needs A Respawn Button and UI To Know Player Is Dead
9. Island Structure: I Created Structure Like Ruins And Buldings (Explain It Later)
10. Player & Control: First-person perspective, WASD movemnet, mouse look, jumps & gravity handled

# game overview image

<img width="1311" height="838" alt="image" src="https://github.com/user-attachments/assets/7dd16d36-f5f6-41b0-98ec-21670826af25" />

# Biggest Problem I Faced

1. Fall Demage: As I Had No Idea, I First Made The Logic, Safe_fall = 5, land_y = 2, fall_s_y = detect the ground, total_distance = fall_s_y - player.y, if total_distancxe >= safe_fall demage(int( total_distance * land_y)), so the fall_s_y lock the value when player do not have ground under him/her then i subtract the fall_s_y with current player.y so that we will get total_distance then i check it is lower or higher then the safe_fall, if higher i call the demage
  
2. Structure: for the structure i visit many software but it need much more exprience and learning, for me building map in the firstperson perspective was much easy but no soft provide it or i did not found one, then what to do, so i thought i will save the coordinates and textures of the entity in one file called map.txt and then load it in the main then i created four function placeblock: place the entity, removeblock: remove the entity, save_map: save the coordinatas and texture, load_map: load the coordinates and texture of entity, after completing map the first three function were not needable so i comment it out so in future i will use it when i need or anyone else need it
3. FPS: it was the biggest problem i face i did not solve it but add the game properties and entity properties to incresse the fps as the real solution needs more time and knowledge but as i am not going to the gaming industry i did not use chunk loading and other method
4. enemy: i created enemy but i had no idea about the behavior so i created the logic and try to implement, it worked but not fully sometime enemy will behave weirdly like flying facing other direction and stuff i used chatgpt but it was no use

# what i learn

i learn more about the oops concept with python as i have separated file for game example: gun.py, enemy,py ,health.py ect so calling the function which is in another file otherthan the main was kinda a tricky because as i thought i  just need to import the file in another file and just call the function after initilization but sometime somethings won't happen as we planned it was throwing error so i research about it and found cross-module method invocation and use it and it worked and i learn functions of the ursina and the core object of the coding, logic building

# installation
so how to install it and play it
1. install ursina - pip install ursina
2. then run the game
3. to exited the game click esc

