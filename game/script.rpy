# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character('John Doe', color = "#192db0")
define a = Character('Angel Doe', color = "#4b1bb3")
define s = Character('Scott Charmin', color ="#750d12")
define m = Character("Mother in Law")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg car_intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
   
    s "Are you nervous?"
    j "Me? Nervous? No way- I mean, are you nervous? Because I'm not nervous."
    s "So you are nervous."
    j "... maybe"

    s "*laughs* I knew it. You've been acting strange all day. What's going on inside your head? Almost feels like you're hiding something."
    j "Well, you told me before that your mother can be..."
    s "Difficult?"
    j "Sometimes.. So, of course I'm nervous to meet her! What if she doesn't like me?"
    s "It's true that she's hard to please... but it'll just be one dinner together. We should be fine."
    j "I guess... but, I'm not really the type of person people would want to bring home to their parents you know? I just don't want to let you down..."
    s "Hey, listen to me. You're not the person who pulled those silly pranks back in high school anymore. You're the person who I fell in love with. You're smart and ambitious, I've never met anyone as amazing as you. If my mother can't see that, then that's her loss"
    j "But... what if..."

    a "Get your shit together, John. Who cares if she doesn't like you? If worse comes to worst, you and Scott were doing fine without her anyways, so what's the big deal?"
    j "Maybe you're right Angel... I think I really needed to hear that."
    a "I just don't want you to overthink this..."
    j "And I appreciate it. Thanks for coming with us today. You're my favorite family member."
    a "Of course, I'm the best."
    a "Wait. Mom and dad cut you off... so doesn't that make me your only family member?"
    j "..."
    a "idiot."

    s " *laughs* Your sister was right you know? About how we don't need my mother's approval. No matter what happens today, we're in this together"
    j "Thanks, Scott..."
    a "Where's my thank you?"
    j "thankkkk youuu Angel"
    a "heh"
    a "How much longer is it till we get to the house? I feel like we've been together in this car forever now"
    s "Actually, we're pulling in now.. Welcome to the Charmin household."

    # John, Angel, and Scott's POV of the front of the house

    scene bg front_door_scene 1

    s "Are you guys ready?"
    j "...Mhm"
    a "Let's just meet the lady and get this over with"

    # knock knock knock sounds

    scene bg door_scene2

    m "..."
    m "You've gained weight, Scott."
    s "Ah ha ha.... Hello, mother... I'd like you to meet-"
    m "Who's the short one. I was only expecting two people."
    
    a "(The short one... IS SHE TALKING ABOUT ME???)"

    j "Um... hello Ms.Charmin."
    s "Mother, as I was trying to tell you, this is my partner John Doe. And this is his younger sister Angel."
    m "How disappointing..."

    j "Um...uh... it's a, um, pleasure to finally meet you Ms.Charmin. Scott told me... um.. so much about you!"
    m "Then he must've told you, I really despise mumbling. Speak up"
    s "Mother, that's enough. Can we come in now?"
    m "*sighs* I suppose.. Though, I wasn't aware three of you will be coming over. There's only food prepared for us, there won't be enough for the short one."
   

    s "That's fine, I can cook something up. C'mon guys, let's head inside."
    m "..."

    j "Um.. th-thank you for welcoming us into your home, Ms.Ch-"
    m "Who even taught you to wear your tie like that? It looks awful."
    a "Just shut up and go in, John."

    #cutscenes added here

    #cutscene 1

    scene bg kitchencutscene1

    "..."

    scene bg kitchencutscene2

    "..."

    scene bg kitchencutscene3

    "..."

    scene bg kitchencutscene4

    "..."

    scene bg kitchencutscene5

    "..."

    scene bg kitchencutscene6


    "..."

    scene bg kitchencutscene7

    "..." 

    #cutscene 2
    scene bg leadup

    "..."

   
    scene bg kitchen


    #Switch to kitchen
    scene bg kitchen
    
    show j neutral 

    j "I'm sorry... I'm so sorry... I just ruin everything..."

    hide j neutral

    show s neutral

    s "Stop that! You didn't ruin anything at all."
    s "I should be the one who should be sorry... after all these years, I thought she would change."
    s "She never did."

    hide s neutral

    show a neutral

    a "Honestly f*ck that b*tch."

    hide a neutral

    show j neutral

    j "Please... Angel... She might hear us."

    hide j neutral
    show a neutral
    a "I'm not gonna apologize for that if SHE CAN HEAR US!! Scott is making such a nice dinner for us and she wanted to repay that BY SLAPPING YOU?"
   
    hide a neutral
    show j neutral

    j "There's not much we can do here..."

    hide j neutral
    show a neutral
    a "Honestly, if that's how she treats people cooking her a meal, I bet there's a ton more at resturants that are just spitting in her food."
    
    hide a neutral
    show j neutral

    j "Why don't we teach her a lesson?"

    hide j neutral
    show a neutral

    a "You don't mean..."

    hide a neutral
    show j neutral
    j "It'll just be like good ol' times.. All over again..!"
    j "It'll be harmless like those pranks that get views on the internet."

    hide j neutral
    show a neutral
    a "No way man, that's Scott's mother you're talking about. She's sh*tty but we can't be that petty. We're not little kids anymore."

    hide a neutral
    show s neutral
    s "She did hurt John... She's no mother of mine anymore."

    hide s neutral
    show a neutral

    a "..."

    hide a neutral
    show j neutral

    j "Sh*tty... like laxatives!"

    hide j neutral
    show a neutral

    a "Sorry what now?"

    hide a neutral
    show j neutral

    j "Let's just put a small dosage into her food. She won't suspect anything!"

    hide j neutral
    show s neutral

    s "Sure, let's do it."

    hide s neutral
    show a neutral
    a "...fine. I'll only look out for you."
    scene bg leadup1
    "..."

    a "She's coming."
    #scene changes - kitchen
    # sprites show
    scene bg kitchen
    "Mother in law enters the scene"

    show s neutral
    s "Mother, apologize to John."

    hide s neutral
    show m neutral

    m "Are you telling me what to do?"

    hide m neutral
    show s neutral

    s "Mother. You hurt John. And you hurt me. I can't continue contact if you're going to hurt the people I love."

    hide s neutral
    show m neutral
    
    m "Scott, please, you're being dramatic right now."

    hide m neutral
    show s neutral
    s "Excuse me?"

    hide s neutral
    show m neutral

    m "We both know it's not true."

    m "I don't know if you're trying to fool yourself, but it's quite pathetic."
    m "You can have your little boy toys and short ones, but you'll always come back to me."

    hide m neutral
    show j neutral

    j "Please don't talk to Scott like that..."

    hide j neutral
    show m neutral

    m "Can't hear you over your mumbling, SPEAK UP."

    hide m neutral
    show j neutral

    j "I...think we left off on a bad footing."

    j "Why don't we sit down and eat Scott's delicious food?"

    hide j neutral
    show a neutral
    a "Yeah, wouldn't you love some... delicious food."

    hide a neutral
    show s neutral

    s "Have a seat mother."

    hide s neutral
    show m neutral

    m "Very well, only because you've made your mother's favorite, Osso Buco"

    hide m neutral
    show s neutral

    s "Don't you deserve the best?"

    "Everyone settles down in their seat"

    hide s neutral
    show m neutral

    m "It's such a shame that mark on your face had faded so quickly. I would've enjoyed this meal a lot more..."

    hide m neutral
    show j neutral

    j "..."

    hide j neutral
    show s neutral

    s "How is the food mother?"

    hide s neutral
    show m neutral
    m "Disappointing. Though, you can't do better than your mother."

    m "It's unusually bitter."

    "*Grumbling noise*"

    m "You have to excuse me..."

    hide m neutral

    "Mother in law leaves"

    "Everyone bursts into laughter"

    show a neutral

    a "That sh*thead doesn't know what's coming"

    hide a neutral
    show j neutral

    j "Do you think I went too far...?"

    hide j neutral
    show s neutral

    s "Did you hear her sadistic tone, John?"

    hide s neutral
    show j neutral

    j "She's still your mom."

    hide j neutral
    show s neutral

    s "Was. After hurting you, she's no longer my mother."

    hide s neutral

    "Moment passes"

    show a neutral

    a "She's been gone for quite some while.."

    hide a neutral
    show j neutral

    j "I think it's gone too far, we need to check up on her."

    hide j neutral
    show s neutral

    s "I'll go. You've been through enough today."

    hide s neutral
    show j neutral

    j "Okay..."

    hide j neutral

    "Silence..."

    show j neutral

    j "Scott's been gone for a while too. Do you think he's okay?"

    hide j neutral
    show a neutral

    a "He's probably trying to help her not sh*t her pants."

    hide a neutral
    show j neutral

    j "We should go check up on them."

    hide j neutral

    scene bg bathroom_door

    "John and Angel leave to find Scott and Mother in Law"

    "Mother in law is unconcious"

    "John slowly faints"
    with pixellate
    #GAME START
    scene bg kitchen

    show s neutral

    s "Oh good, you're awake."
    scene bg kitchen

    hide s neutral
    show j neutral

    j "What... happened?"

    hide j neutral
    show s neutral
        
    s "Okay, don't freak out but..."

    hide s neutral
    show a neutral

    a "YOU FUCKING KILLED HER"

    hide a neutral
    show j neutral

    j "Wait, what???"

    hide j neutral
    show a neutral
    a "I always knew your stupid pranks were terrible, but this time you went too far!!"
    a "Scott's mother died from laxatives because of YOU!"


    hide a neutral
    show s neutral

    s "Well we don't know if she's actually dead!"

    hide s neutral

    "Scott leaves the kitchen"

    #scott comes back

    show s neutral
    s "Yeah she's dead."

    hide s neutral
    show j neutral

    j "I didn't know it would go so far... People on reddit never mentioned it can kill a person.."

    hide j neutral
    show a neutral

    a "YOU'RE TAKING THESE IDEAS FROM REDDIT????"

    hide a neutral
    show j neutral

    j "I didn't mean for this to happen!"

    hide j neutral
    show s neutral

    s "Alright guys, let's all calm down for now."

    hide s neutral
    show a neutral

    a "CALM DOWN?? YOUR MOTHER IS DEAD, YOUR BOYFRIEND MURDERED HER! AND YOU WANT US TO CALM DOWN?"

    hide a neutral
    show j neutral

    j "Oh god... Scott.. I'm so sorry."

    hide j neutral
    show s neutral

    s "Hey, it's okay, you didn't mean for this to happen. It was an accident!"

    hide s neutral
    show a neutral

    a "His \"accident\"..." 
    a "IS CALLED MANSLAUGHTER"
    a "We need to go to the police."

    hide a neutral
    show j neutral

    j "Police? No no no.. Please don't..!"
    j "I didn't mean for this to happen..! I don't want to go to jail! Please don't.."

    hide j neutral
    show s neutral

    s "No one is going to call the police."
    s  "Angel just remember, you'll ALSO have to face the consequences too."
    s "We're all accomplices here."

    hide s neutral
    show a neutral

    a "..."

    hide a neutral
    show s neutral

    s "We have to do something about this that DOESN'T involve the police."

    hide s neutral
    show j neutral

    j "... Where do you guys keep the cleaning supplies?"

    hide j neutral
    show a neutral

    a "Why?"

    hide a neutral
    show j neutral
    
    j "We need to hide the body."

    #Cover the body segment

    j "First thing's first, let's cover her body with something.."
    hide j neutral
    show s neutral
    s "Well, We do have a tarp somewhere in the garden."

    #Navigation tool highlights
    #Player can go to different areas

    j "First thing's first, let's cover her body with something.."
    s "Well, We do have a tarp somewhere in the garden."

    "{i} Objective: Find the tarp in the garden {/i}"














    


    window hide
    mapscroll kitchen gloves bleach hydrogenperoxide
    window show

    #Cover the body segment

    #if the player goes to wrong room, characters will show up

    #Wrong place - MIL BEdroom


    show a neutral
    a "Shouldn't be in here stupid, you're finding the tarp in the garden." 
    hide a neutral

    #bathroom

    show s neutral
    s "Let's not go in there for a while.."
    hide s neutral

    #Scene change - garden
    #Sprites will show up

    show s neutral
    s "The tarp is over there by the under the table."
    hide s neutral

    #if player clicks anywhere else that's not under the table

    show s neutral
    s "That's not under the table"
    hide s neutral

    #After player hovers and click over tarp to know it's clickable

    show j neutral
    j "We got the tarp."
    j "We're going to need some cleaning supplies too."
    
    hide j neutral
    show s neutral

    s "Hey... do you remember those true crime shows we used to watch all the time in high school?"

    hide s neutral
    show j neutral

    j "What about them?"

    hide j neutral
    show s neutral

    s "Well... what do those people normally get when cleaning a body?"
    #John tells the needed supplies to hide body
    hide s neutral

    menu:
        "Gloves":
            pass

    show j neutral
    j "We need gloves to cover our fingerprints.. "
    hide j neutral
    menu:
        "Bleach and hydrogen peroxide":
            pass
    show j neutral
    j "Some bleach would help remove the blood stains but hydrogen peroxide gets rid of the blood stains under UV light"
    
    hide j neutral
 

    show a neutral
    a "You sound a bit too prepared for this..."
    hide a neutral

    "{i} Objective: Find the cleaning supplies {/i}"
    # Player will now navigate and press on needed items for the game, take a look on diagram for more info

    #Gloves

    #MAP SCROLL - Gloves

    show j neutral
    j "The gloves are on the table to my right... Easy find"
    hide j neutral

    #gloves are now clickable and player picks it up

    show j neutral
    j "I found the gloves"

    #END MAP SCROLL

    j "Now we need the bleach and hydrogen peroxide."

    j "Would they be in the bathroom?"

    hide j neutral
    show s neutral

    s "No... It wouldn't"

    s "When I was a child, my mother would constantly clean anything she deems as dirty..."
    s "She wouldn't put any cleaning products in there"

    hide s neutral
    hide s neutral
    show j neutral
    j "Where would she put it?"

    hide j neutral

    show s neutral
    s "If I can remember... It should be somewhere in the kitchen"

    

    #Scene change/player goes to kitchen 
    #if player picks the bottom cabinet (take ref from diagram)
    #items will be clickable when hovered over

    #if player picks up bleach

    hide s neutral

    #MAP SCROLL - BLEACH AND HYDROGEN PEROXIDE

    show j neutral
    j "Here's the bleach.."

    show a neutral
    a "I can't believe you're going through with this."
    hide a neutral

    #if player picks up hydrogen peroxide

    show j neutral

    j "Hydrogen peroxide... best way to hide the blood stains."

    hide j neutral
    show s neutral
    s "Who knew those true crimes show paid off?"
    hide s neutral

    #END MAP SCROLL

    #After player collects everything 
    #scene changes to the front of the bathroom/cutscene

    scene bg bathroom_door

    show s neutral

    s "Okay, now that we have everything let's head back to the bathroom."

    hide s neutral
    scene bg reveal

    a "Is he... crying?"

    j "I... feel like a monster. This is all my fault. Even though he told me that his mother was horrible. "

    a "I'm not justifying your actions, you are awful, but Scott loves you too much yo blame you."

    a "This man literally comforted you by saying it was an accident."

    a "'An accident-'"

    a "That's not a normal response to someome who just killed their mother."

    a "It was weird at first... how Scott was so calm when everything happened."

    a "But I guess he's been hiding his true feelings this entire time."

    scene bg bathroom_door

    "Silence as they look at Scott's back slowly stop shaking"

    a "Well, she was full of sh*t anyways.."

    #Scene change to the outside of the bathroom

    show s neutral

    s "Alright, it's done."
    hide s neutral
    show j neutral

    j "Scott... I'm sorry. You should stop, I can clean the rest myself. "

    hide j neutral
    show s neutral

    s "You have nothing to apologize for. It's okay... I don't want you to face this alone. "
    hide s neutral
    show s neutral

    j "It's fine. I have to deal with the mess I made."
    hide j neutral

    with dissolve
    #cut scene

    scene bg bathroomscene1

    j "{i}What am I doing? {/i}"

    scene bg bathroomscene2

    j "How did I get to this point? It was suppose to be a prank but now I'm a murderer."

    scene bg bathroomscene3

    j "And I dragged Scott and Angel into my mess too..."

    scene bg bathroomscene4

    j "Oh god, Scott... I can't believe I did this to him. He's been so good to me."

    scene bg bathroomscene5

    j "He still loved me when I was at my worst. I thought I became better for him... but now... nothing changes."

    #John starts to break down and has a panic attack. Unable to breath and catch his breath.

    #Scott knocks

    scene bg bathroomscene6

    j "I never changed. I can't change. How can he ever forgive me?"

    scene bg bathroomscene7

    play audio 'audio/sound knock.mp3'
    s "Hey are you okay in there?"

    #(heavy breathing)

    scene bg bathroom

    show j neutral

    j "I'm fine..! I'm doing okay.. Don't come in here, I got it."

    hide j neutral

    play audio 'audio/sound door_open.mp3' 
    stop audio fadeout 0.5

    show s neutral
   
    s "John? Are you okay? What's happening?"

    hide s neutral
    show j neutral

    j "I already told you, I'm fine. Please leave me alone."

    hide j neutral
    show s neutral

    s "How can I leave you alone? You're clearly not fine."  

    
    hide s neutral
    show j neutral

    j "I'm sorry. I'm sorry for everything. This is all my fault. This wouldn't have happened if you had never met me."

    hide j neutral
    show s neutral

    s "What? What are you saying John?"

    hide s neutral
    show j neutral

    j "She's dead now because of me. I never meant to hurt you. I always ruin things, but I never wanted to ruin things with you."
    j "I'm not good enough for you. I don't know why you're still here."

    hide j neutral
    show s neutral

    s "John stop it... You didn't ruin things with me and you won't. I will always love you."

    hide s neutral
    show j neutral

    j "Why? Why do you still love? I'm a mess and you deserve so much more."

    hide j neutral
    show s neutral

    s "Don't tell me who I should love. I only want you in my life. We will get through this together."

    hide s neutral
    show j neutral

    j "Why are you like this?"

    hide j neutral
    show s neutral

    s "What do you mean?"

    hide s neutral
    show j neutral

    j "{b} I killed her. {/b}"

    j "I killed her. And now she's dead."

    j "Why are you acting like that didn't happen? Like I did a minor mistake?"

    hide j neutral
    show s neutral

    s "John, to be totally honest."

    s "I'm{b} really terrified {/b}."

    s "I don't know what's going to happen to us, but all I know is that I want to protect you..."

    s "It seems really silly, but you're precious to me."

    s "My mother was never the best to me. I just want us to all move on."

    s "I know my reaction doesn't seem normal... but I've mourned a long time ago"

    hide s neutral

    "{i} What does he mean by that? {/i}"

    show s neutral

    s "As long as you're safe, that's all that matters."

    hide s neutral
    show j neutral

    j "Do you really mean that?"

    hide j neutral
    show s neutral

    s "Of course. I love you."
    s "And I'll always reassure you even at a time like this so you'll know I love you."

    hide s neutral
    show j neutral

    j "I love you too..."

    hide j neutral


    show s neutral
    s "Let's clean up together, okay?"

    hide s neutral
    show j neutral
    j "Okay.."

    hide j neutral
    
    with dissolve

    scene bg bathroom_door
    #cutscene end

    show a neutral
    a "What's next?"

    hide a neutral
    show s neutral

    s "We need to find a place to hide the body."

    hide s neutral
    show a neutral

    a "No sh*t sherlock. I meant how are we gonna do that? I don't think we can exactly pull off carrying a body bag around."

    hide a neutral
    show j neutral

    j "You're right. I'm not really sure what to do next..."

    show a neutral

    a "..."

    hide a neutral
    show s neutral

    s "..."

    hide s neutral
    show j neutral

    j "..."

    hide j neutral

    scene bg phonescene1

    j "Let me pull up reddit real quick"

    a "Oh god."

    scene bg phonescene2

    s "I trust you honey!"

    a "Oh god."

    #cutscene reddit
    scene bg phonescene3

    "{i}JohnPoe: Where to hide (fake) body to scare MIL?{/i}"
    "{i}Hey guys, so I want to do a funny prank on my MIL by hiding this fake body bag around my house. {/i}"
    "{i}She's coming home soon lol so I need to find a place around my house quickly. Do you guys know the best spot?{/i}"
    
    scene bg bathroom_door
    show j neutral

    j "Alright, I posted it."

    hide j neutral
    show a neutral

    a "There's no way this'll work."

    hide a neutral
    show s neutral

    s "Looks like you already got some replies."

    hide s neutral

    scene bg phonescene3

    "HisKitten: Omg lool- How did you come up with these stuff? Personally a bathroom might be funny cause she'll sh*t herself!"
    "HerMod: That would be so crappy 8)"
    "Alone4Lyfe: Too many sh*tty puns here"

    j "A little bit on the nose..."

    "VickydaVinki: How about her closet? You can hide it in a bunch of clothes?"
    "PuntasticSadness: Lame L ratio"

    s "No, that's not good either"

    a "Ouch look at all that downvotes..."

    "NotaKiller: Garden? Normally that's a good spot to hide actual bodies, so why not a fake one? uwu"
    "ThrowAway68: agree"
    "DrFBI: lowkey sus - r u a murderer?"

    j "This last one might work... There was a greenhouse here."

    #Cutscene end

    scene bg bathroom_door

    show a neutral

    a "Do we even have the supplies to even pull it off?"

    hide a neutral

    show s neutral

    s "Well, my mother used to garden a lot. I;m sure we have plenty of supplies lying around."

    hide s neutral
    show j neutral

    j "Like what?"

    hide j neutral
    show s neutral

    s "If we're putting her in the green house, shovels are a great starter. Perhaps fertilizers too?"

    s "It'll be hard to move around an open tarp, so we would also need to secure the body.. But there's no rope I think"

    hide s neutral
    show j neutral

    j "I saw some black cords in her closet. WOuld we be able to use that to tie the body?"

    hide j neutral
    show s neutral

    s "That could work!"

    hide s neutral
    show j neutral

    j "Do you really think we can pull this off?"

    hide j neutral
    show s neutral

    s "No matter what, I'll always support you."

    hide s neutral
    show a neutral

    a "You guys seem closer after cleaning..."

    hide a neutral


    #NEW OBJ Find tools to hide body

    #MAP SCROLL - cables 

    "{i} New Objective: Find tools to hide body {/i}"

    show j neutral

    j "Okay, let's do this. I should get the cord from the bedroom first."

    hide j neutral

    #player enters the bedroom and grabs cord, automatically triggers dialogue - note John and Scott are in the room 
    #MAP SCROLL END

    show j neutral
    

    j "I got the cables. Now we just need to get the rest."

    hide j neutral

    scene bg mil_room

    show s neutral

    s "After this, we can pretend like none of this ever happened. We can move on and live peacfully"

    hide s neutral
    show a neutral

    a "Wait... wouldn't people realize Scott's mother's sudden disappearance?"

    hide a neutral
    show s neutral

    s "We shouldn't worry about that. No one liked her anyways, and she didn't exactly have friends. No one will notice."

    hide s neutral
    show a neutral

    a "Sure... but what if someone DOES notice? Like her neighbors? Or even the mailman. This isn't going to work out."

    hide a neutral
    show s neutral

    s "How about we forge a letter... to explain why she's gone?"

    hide s neutral
    show j neutral

    j "Angel...?"

    hide j neutral
    show a neutral

    a "No way. I'm not doing that. I'm not forging these letters for you."

    hide a neutral
    show j neutral

    j "Please Angel, you forged signatures all the time. THey were perfect replicas."

    hide j neutral
    show a neutral

    a "That's only to save your a**. We were young and I was stupid. Now you're using that agaist {i}me{/i}?"

    hide a neutral
    show j neutral

    j "Angel, I need you. We need you. Please help me one last time."

    hide j neutral
    show a neutral

    a "I won't do that. It's a federal crime."
    hide a neutral
    show s neutral

    s "What's one more felony? At this point, it can't be worse than murder."

    hide s neutral
    show j neutral

    j "Scott's right. We're already in too deep."

    j "This is one thing that might help us get out of jail."

    hide j neutral
    show a neutral

    a "...fine. But after this is all over, I'm never talking to you again."

    hide a neutral
    show j neutral

    j "Angel, you don't mean that right?"

    hide j neutral
    show a neutral

    a "They were right about cutting you off. I should've listened to them. I shouldn't have come here."

    hide a neutral
    show j neutral

    j "..."

    hide j neutral

label letter_scene:

    scene bg desk

    "If you're seeing this, then I'm already gone. There's no reason for me to stay. I've decided to run away because..."

    menu: 
        "life has been miserable, I needed to go.":
            pass
        "I have found a new chance at life, with someone else.":
            pass
        "No one will notice if I disappeared":
            pass
    
    "This was not an easy decision to make. Although I am certain this is the path I am willing to take. If you read this letter..."

    menu:
        "don't bother trying to find me.":
            pass
        "discard this letter and live your own life.":
            pass
        "Keep this letter private between us.":
            pass
        
    "There's not much else to say. I don't plan on being found, so don't look for me."
    "Goodbye."

    #Resumes

    scene bg mil_room

    show s neutral
    s "Now let's do the rest... We need fertilizer and a shovel."

    hide s neutral
    show j neutral

    j "Both should be in the garden..."

    hide j neutral

    "{i} Continued Objective: Find remaining tools {/i}"

    #MAP SCROLL - Fertilizer and Shovel


    #Fertilizer is found in green house

    scene bg garden

    #After player picks up fertilizers

    show j neutral

    j "... organic fertilizer"

    hide j neutral
    show s neutral

    s "So... animal shit?"

    s "How fitting."

    hide s neutral

    #Shovel after picked up

    show j neutral

    j "Shovel.. am I seriously going through with this?"

    hide j neutral

    #After pickig up the item

    #MAP SCROLL END

    #Scene in green house

    show j neutral

    j "Okay, that should be everything. Now to just... bury her."

    hide j neutral
    show s neutral

    s "Where's Angel?"

    hide s neutral
    show j neutral

    j "I think she's avoiding me... Is she really serious about not talking to me again?"

    j "I know she's upset, but we had no choice. RIght? "

    j "Some brother I am... Constantly dragging her down to clean my sh*t" 
    j "Now she's saying our parents were right, she doesn't mean it right?"

    hide j neutral

    show s neutral

    s "{b}I have a bad feeling about this{/b}"

    hide s neutral

    show s neutral at left

    s "I'm going to look for her."


    show j neutral at right
    j "Oh alright, go ahead. I don't think she'll follow us though."
    
    
    hide s neutral
    hide j neutral

    "{i} Scott leaves the greenhouse {/i}"

    show j neutral

    
    #Scott leaves

    j "Let's finish this."

    #Play audio scream

    scene bg garden

    play audio 'audio/sound angel_scream.mp3'
    "{i} A familiar scream echoes inside the house {/i}"

    show j neutral

    j "What was that? Angel??"

    j "I think the screams came from the bedroom. I should check it out and see if she's okay."

    hide j neutral


    scene bg kitchen

    show j neutral
    "No... not here. I think the screams are coming from the bedroom."

    hide j neutral
    #When player reaches the bedroom

    #I hear her in the closet..

    

    scene bg mil_room

    play audio 'audio/sound door_rattling.mp3'

    show j neutral

    j "Damn. The door's locked."

    j "Angel, it's me. Are you okay?"

    j "Is this about earlier? I'm sorry..."

    j "Please come out and talk to me. We can work through this together."

    hide j neutral
    show s neutral at right
    show j neutral at left

    #door open
    #Scott's sprite comes out

    j "Scott? What are you doing in there? Is Angel alright?"

    s "I think we should leave. Angel needs some space right now"

    j "But... I heard a scream... I need to see for myself that she's okay."

    s "She REALLY needs some space right now John"


    #Thuds sound

    play audio 'audio/sound thud.mp3'
    "{i}Thuds against the door"

    j "That's definitely not okay. Angel???"

    s "..."

    j "Scott? What's going on??"
    #Screaming

    play audio 'audio/sound angel_curse.mp3'
    "{i}Angel Screaming{/i}"

    hide s neutral
    hide j neutral

    a "LET ME OUT MOTHER F*CKER!!!"

    show s neutral

    s "Sh*t..."

    hide s neutral
    show j neutral

    j "Angel??"

    hide j neutral
    
    play audio 'audio/sound door_kick.mp3'
    "{i}Angel kicks open the door to reveal she had been tied up and looked roughed{/i}"

    show a neutral at center

    a "YOU B*TCH!"

    show j neutral at left


    j "What's going on???"

    a "Soctt caught me trying to call the police and TIED ME UP!"

    j "You were calling the police...?"

    a "THAT'S THE PART YOU FOCUS ON???"

    j "Scott... why did you do this to Angel?"

    show s neutral at right

    s "I had to. She was going to turn us in to save herself. I don't want to lose you because of her."

    j "But... she's bleeding."

    a "John, snap out of this. Scott is not a good person. Don't listen to him."

    s "Why would he not listen to you? Angel was only thinking of saving herself, she was going to cut you off, remember? I would never do that to you. I can't lose you. We're in this together."

    hide j neutral
    hide a neutral
    hide s neutral

    menu:
        "I trust you Angel.":
            jump angels_route
        "I believe you Scott.":
            jump scotts_route

label angels_route:

    show s neutral

    s "No no no no no.... Please believe me! I did it for you. All of this is for you!"

    hide s neutral
    show j neutral

    j "Scott... please. Just leave me alone, I need some time to collect my thoughts."

    hide j neutral
    show s neutral

    s "Okay... I'll give you some space. But please, reconsider this."

    hide s neutral

    #Kitchen scene
    with dissolve
    "{i}John and Angel leaves to the kitchen{/i}"


    show a neutral 

    a "I'm sorry."

    hide a neutral

    scene bg kitchen

    show a neutral at right

    show j neutral at left

    j "There's nothing to be sorry about."

    a "I know it's not easy to pick me over him."

    j "Scott was all that I had..."

    a "I know."

    j " No.. you really don't. When mom and dad disowned me, I was at my lowest point in my life. "

    j "I fell in love with Scott at the lowest point of my life. He knew who I was, yet ...he allowed himself to fall for me."

    a "I didn't know that."

    j "How could you? You never contacted me."

    a "After you left, I was under scrutiny by our parents. "

    a "Everything I did, what food to eat, what career to take, I did it for them. "

    a "I never lived for myself, even now.. I'm glad I can be in your life now."

    j "You said this was the last time we'd talk."

    a "I only said that because I was hurt. I know it's not an excuse to give after everything we've been through. I shouldn't have said that. I'm sorry."

    j "I want to believe you."

    j "I was so angry back then, I would not have never believed you. I never trusted anyone at that point, including Scott. But he stuck around and helped me become better."

    j "I thought I was better."

    j "He's been protecting me from this sh*t world. Protecting me when I had no one."

    j "He still protecting me after his {i}his own mother{/i} died..."

    a "Doesn't it feel strange how quickly he was to help?"

    j "What do you man by that?"

    a "I mean {i}his mother just died{/i} Scott never had the time to process it, yet his first thought was to {i}help you{/i}?"


    a "Why was he so quick to hide her body?"

    j "You don't think..."

    hide j neutral
    hide a neutral

    #Audio plays thuds
    "{i}THUDS{/i}"
    play audio 'audio/sound thud.mp3'

    show s neutral at left


    s "John. Don't listen to her."

    show a neutral at right

    a "You b*tch, he's not going to believe you after evrything we've been through."

    s "Why would I ever hurt him? I lov him so much..."

    show j neutral at center

    j "Scott... {i}Did you kill your mom{/i}?"

    s "Just listen to me. Angel does NOT have your best interest. She wanted to call the police on you when it happened."

    s "And she still tried to call the police after everything we've been through."

    s "Only reason she stopped in the beginning was because {b} she knew {/b} she was part of this mess."

    a "I'm tired of running away. I'm tired of hiding our mistakes. We need to take this head on."

    s "How can we trust you?"

    j "Scott, did you kill her?"

    s "Honey, listen to me. I would {b} NEVER {/b} hurt you like Angel did."

    s "I don't know what I would do without you!"

    j "Did you kill her?"

    s "You're not listening to me. Why don't you trust me? After all we've been through."

    j "How can I trust you if you can't even answer this?"

    s "How can you just say that? We love each other. Why would you trust her over me?"

    j "If you're not going to tell me... I don't think we're right for each other."

    s "{i}No no no no...{/i}"

    s "{i}No no no no no no no....{/i}"

    hide s neutral
    hide a neutral
    hide j neutral

    #scene changes angel route

    scene bg angel_route

    s "Please... You don't mean that, do you?"

    j "I do. No matter how much I love you, I{b} cannot {/b} trust you."

    s "I did this for you. Everything I did was for you."

    j "Why do you keep saying that?"

    s "We were never going to be happy for as long as she lived."

    a "You resorted to murder??"

    s "I had no other choice. There was no other way around this."

    j "How could you... You made me believe that {i}I KILLED HER{/i}"

    s "I'm sorry... I'm so sorry. I did what I can to protect you. I would've told you sooner if {b} she {/b} wasn't in the way."

    a "How could you manipulate my brother like that? He {i}LOVED{/i} you."

    a "And you took advantaged of his kidness... you turned it into your own sadistic game."

    s "Stop talking...! This wouldn't have happened if it wasn't for you..."

    a "No Scott. This wouldn't have happened if you didn't {b} spike her food {/b}"

    s "You don't understand me at all."

    j "Did you do it?"

    #Scene change

    scene bg kitchen

    show s neutral

    s "It was our love that killed her...! Your laxatives and my cyanide. Our love killed her."

    hide s neutral
    show a neutral

    a "Get away from us."

    hide a neutral
    show s neutral

    s "WHY? I answered everything you asked me to. I did everything for you John, please tell her she's being unreasonable."

    hide s neutral
    show j neutral 

    j "We need to go."

    show s neutral at left

    s "NO PLEASE!"

    hide s neutral
    hide j neutral

    "{i} John and Angel hurridely escapes the house. {/i}"


    "{i} Without a moment of hesitation, Scott quickly follows them. {/i}"

    #play siren noises

    #scene changes to pollice end

    scene bg ending

    "{i}FREEZE! PUT YOUR HANDS IN THE AIR!{/i}"

    "{i}ANYTHING YOU CAN SAY CAN AND WILL BE AGAINST YOU IN THE COURT OF LAW!{/i}"

    "Shit..."

    return



label scotts_route:

    show a neutral

    a "John, what the f*ck are you saying? Do you see me? Look at what that PSYCHO did to me!"

    hide a neutral
    show j neutral

    j "Angel, you've been against me from the start. How can I believe you now?"

    hide j neutral
    show s neutral

    s "Angel, just stop. We're not going to believe you after all of your deception"

    hide s neutral
    show a neutral at right
    

    a "You're one to talk b*tch."

    show j neutral at center

    j "ANGEL! That's enough."


    a "John, please, you have to believe me. I'm your sister, you can trust me when I tell you, Scott is not who he says he is."

    j "Stop talking Angel."

    j "You have been trying to call the police since the beginning."

    j "You made us believe that you CARED about me by coming. Only to leave when it's most convenient."

    a "That's not it at all."

    show s neutral at left

    s "Do you want me to shut her up dear?"

    hide s neutral


    j "..."

    a "No no no please don't..."

    a "John? You can believe me, right?"

    j "..."

    s "Angel, you have been a burden since the beginning. You need to be quiet."

    a "John, please help me."

    j "..."

    a "I know you're still in there."

    a "Please..."

    hide a neutral
    hide j neutral

    "{i} Scott and angel both disappear into the closet {/i}"
    play audio 'audio/sound angel_scream.mp3'
    " {i}followed by angel's scream {/i}"

    #Scott comes back in frame

    scene bg scott_route

    s "Sorry about that my darling."

    #Scene change cut scene Scott's route

    j "..."

    s "I know that this wasn't an easy decision to make."

    j "Why did you killed her?"

    s "Killing is such a harsh word... I only did what's needed to be done."

    j "By killing?"

    s "She was a burden to our lives and a stain that needs to be removed."

    s "The second you came to my life, I knew I had to protect you."

    j "Is that why you killed your mom?"

    s "It was our love that killed her."

    s "Your funny laxatives and my toxic cyanide. We were made for each other."

    j "Was this planned since the beginning?"

    scene bg mil_room

    show s neutral at left

    s "I knew no matter what happened, she would always be in the way. I wanted our happiness."

    show j neutral 

    j "Weren't we happy before?"

    s "We were. Aren't we happier now?"

    j "...I don't know."

    s "That's okay that you don't know. I'll be here to support and guide you."

    j "I know I've asked this before... but why me?"

    s "What do you mean?"

    j "You answered it before but now I don't know if that's even true."

    s "All I've said about you has been truthful."

    s "I never wanted to hurt you... I'm sorry for holding the truth in until now."

    s "Do you remember the first time we met?"

    j "Yeah, can't exactly forget someone who stopped my notorious pranks."

    j "You were the kindest person in the student body. You helped me get out trouble more than I would like back then."

    s "Not exactly the first time..."

    j "Have we met before that?"

    s "It was back in junior high, I didn't have a good life at home and school wasn't exactly my safe haven either."

    s "Every day I gave myself reasons to be here, until one day I couldn't find any."

    s "Moments before what could've been the end, you {b}saved me{/b}."
    
    s "Even when you didn't know it, you saved me."

    j "..."

    s "You came up to me and gave me my blazers."

    s "You noticed I left without it and you searched the entire campus to find me..."

    s "You didn't even know me."

    s "Your act of kindness towards me was a lot more than what my mother had given me my entire life."

    j "I didn't know that."

    s "It's okay, I don't hold it against you."

    s "When you came into my life, it was almost as if fate had wanted our lives to intercept."

    s "You were my light that I needed to protect."

    j "Is that why you killed them?"

    s "I was hurting for a very long time before I met you. I don't want either of us to ever experience what I felt."

    s "They were an interference to our happy lives."

    s "They had to go."

    j "Isn't that selfish? To live that way?"

    s "I don't see why it's selfish to be happy."

    s "Why should I live for others who treats me like sh*t when they can?"

    j "You're right."

    j "{b} I love you {/b}"

    s "And I love you the most my dear."

    s "I don't know what will happen now, but as long as you're here, I'm okay."

    s "Let's leave this prison together."

    hide j neutral
    hide s neutral

    scene bg kitchen

    "{i} John and Scott both embrace each other lovingly"
    "{i} Leaving the Charmin House locking each other's arm"

    # - scene changes - 

    #sounds of running door opening, sirens

    scene bg ending

    "Officer: FREEZE! PUT YOUR HANDS IN THE AIR"

    "Officer 2: ANYTHING YOU CAN SAY CAN AND WILL BE AGAINST YOU IN THE COURT OF LAW"

    "Shit..."

return 