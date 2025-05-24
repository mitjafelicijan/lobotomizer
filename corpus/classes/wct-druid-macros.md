# WoW Classic Druid Macros

* Author: [Pippina](https://www.warcrafttavern.com/author/pippina/)
* Date: September 30, 2019
* Updated: December 10, 2020
* Expansion: [WoW Classic](/wow-classic/)

### Contents

1. [Shapeshifting / Powershifting / Mounting](#ftoc-shapeshifting-powershifting-mounting)
   1. [Dire Bear Form](#ftoc-dire-bear-form)
   2. [Cat Form](#ftoc-cat-form)
   3. [Aquatic Form](#ftoc-aquatic-form)
   4. [Travel Form](#ftoc-travel-form)
   5. [Mount Macro](#ftoc-mount-macro)
   6. [Cancel Form](#ftoc-cancel-form)
2. [Target Icons](#ftoc-target-icons)
   1. [Star / Golden Star of Healing](#ftoc-star-golden-star-of-healing)
   2. [Orange Circle / Condom of Tanking Protection](#ftoc-orange-circle-condom-of-tanking-protection)
   3. [Pink Diamond](#ftoc-pink-diamond)
   4. [Green Triangle](#ftoc-green-triangle)
   5. [Moon](#ftoc-moon)
   6. [Square](#ftoc-square)
   7. [X](#ftoc-x)
   8. [Skull](#ftoc-skull)
   9. [Clear Icon from Target](#ftoc-clear-icon-from-target)
3. [Offensive Macros](#ftoc-offensive-macros)
   1. [Faerie Fire](#ftoc-faerie-fire)
   2. [Attack Macros](#ftoc-attack-macros)
4. [Support Spells](#ftoc-support-spells)
   1. [Innervate](#ftoc-innervate)

I never used macros back in the original game, but I kept hearing about how useful they were. So this time around I learned what can be done with macros, and wrote a bunch to replace most of my spells in game.

Shapeshifting / Powershifting / Mounting
----------------------------------------

### Dire Bear Form

This macro is written for Dire Bear Form because I’m level 44 right now. I had to change the wording in the macro once I learned Dire Bear. This same macro works for regular Bear Form, but you gotta change the wording up. Just delete the word ‘dire’ from the macro and make it say ***/cast bear form*** if you don’t have the dire bear skill yet.

The macro shifts directly to Dire Bear form. Automatically dismount, cancel current form, cancel any Blessing of Salvation, stop casting, go directly to bear form. It cancels Blessing of Salvation because this aura reduces your threat. Sometimes you might be doing a DPS role with Salvation and have to suddenly take over for a dead tank, so this automatically drops the Salvation buff in the process without needing to think about it.

I also added /stand to the macro so I can go directly to bear from while sitting. Whenever I want to signal to my healer and casters to sit down and drink, I drop form and sit and wait. Once it’s time to go, I go back into bear form. Now I can directly shift to bear form while sitting down.

Since this can go directly from Bear Form > Bear Form, pressing this macro while in Bear Form is a quick power shift for extra rage.

**Note:** It appears that dismounting trips a shape shifting cooldown, so it cannot go directly from being mounted to bear form. But you can double tap this macro and go from mounted > dismounted > bear form.

```
#showtooltip dire bear form
/dismount
/cancelform
/stand
/cancelaura blessing of salvation
/stopcasting
/cast dire bear form
```

### Cat Form

Shift directly to Cat Form. Automatically dismount, cancel current form, stop casting, go directly to Cat form. Since this macro allows you to go directly from Cat > Cat, pressing this macro in cat form lets you power shift for extra energy. Unlike the bear form macro, this one won’t cancel Blessing of Salvation because that’s a helpful buff to have as DPS. I also added /stand so I can go directly into cat form while sitting.

**Note:** It appears that dismounting trips a shape shifting cooldown, so it cannot go directly from being mounted to cat form. But you can double tap this macro and go from mounted > dismounted > cat form.

```
#showtooltip cat form
/dismount
/cancelform
/stand
/stopcasting
/cast cat form
```

### Aquatic Form

Shift directly to Aquatic form. Automatically dismount, cancel current form, stop casting, go directly to Sea Lion. Yes, if you’re in the water the game should have automatically kicked you off your mount anyway, but I include /dismount anyway just in case something is lagging. No harm in /dismount being there even if you’re already dismounted.

```
#showtooltip aquatic form
/dismount
/cancelform
/stopcasting
/cast aquatic form
```

### Travel Form

Directly shift to travel form. Unlike Cat/Bear/Water forms, pressing this while inside travel form cancels travel form. There is no reason to power shift from travel > travel, so this macro lets you go directly to travel form from any form, and also lets you cancel travel form while inside. I also added /stand so I can cast travel form directly from sitting.

**Note:** It appears that dismounting trips the global cooldown, so it cannot go directly from being mounted to travel form. But you can double tap this macro and go from mounted > dismounted > travel form.

```
#showtooltip travel form
/dismount
/stand
/cast [stance:1] dire bear form; [stance:2] aquatic form; [stance:3] cat form
/cast travel form
```

### Mount Macro

The game doesn’t allow you to mount up from within a form. You have to go through the extra step to exit form and then mount. Which is fine, but it adds time and sometimes you just gotta mount **NOW** because fractions of a second could be the difference between avoiding a gank and getting your corpse teabagged. So I wrote this macro to make a single-button-press affair to mount up from any form. Nice thing is that unlike dismounting > entering a form, cancelling your form does not trigger any global cooldown so this does not require a double tap. Just a single key press and your mount summon begins immediately, regardless of current form. I also added /stand so I can summon my mount directly while sitting.

```
/stopcasting
/cancelform
/stand
/use 4 9
```

Note that this relies on my mount being in a specific slot in a specific bag. In my case, I keep my mount in the bag all the way to the left (Bag #4) and it’s in slot # 9 within that bag. For visual reference that is here in my 12 slot bag:

![WoW Classic Inventory](https://i.imgur.com/xjxiz5H.png)

You’re gonna need to experiment and tailor this macro to your specific bag layout and where you keep your mount.

### Cancel Form

Combination drop form and dismount button. Sometimes you just wanna go back to normal form so you can speak to NPCs or whatever.

```
/cancelform
/dismount
```

Prowl  
Go directly to stealth. Or if you’re already If you’re already in stealth then pressing this button exits stealth and leaves you in cat form. If you’re in cat form, it simply enters stealth without powershifting you back into cat and wasting mana. If you’re not in cat form, it automatically enters cat form and drops you into stealth. If you’re in a different form, it automatically drops that form, enters cat form, and enters stealth. If you’re casting, it stops your cast and immediately drops your ass into cat form and then stealth with a single key press. If you’re mounted and need to jump off your mount and hide your ass, it drops you from your mount, enters cat form, and enters stealth.

**Note:** Apparently dismounting triggers the shapeshifting cooldown, so you can’t go directly from mounted > dismounted > cat form > stealthed. So when using this from on a mount you gotta double tap. Be extra aware of this delay because if you wait too long to double tap this to go from mounted > dismounted > stealthed then you may end up remaining visible for a second long than you expected. This results in accidentally pulling mobs you wanted to stealth behind, getting caught by opposing players, etc… so be ware of this cooldown and plan for it.

```
#showtooltip prowl
/dismount
/stopcasting
/cancelform [stance:1] Bear Form; [stance:2] Aquatic Form; [stance:4] Travel Form
/cast [nostance] cat form
/cast [nostealth] prowl
/cancelaura [stealth] prowl
```

Target Icons
------------

Assign an icon over the head of the target. Assign these macros to the keyboard somewhere and press a key instead of right-clicking the target’s unit frame and going through menus to find the icon you want. I have these bound to keys 0-8 on my keypad and it’s extremely quick to assign and clear target icons on the fly. Note that these use the /run command, which the game client will warn you about. The /run command can be used for some advanced stuff, so you don’t want to use /run commands that you don’t understand. Just click the ‘accept’ button and the game won’t bother you again.

**Update:** Apparently there are direct keybinds for these icons. I did not know they were there. There is no need for these to exist as macros by themselves, just assign a keybind directly to them through the keybind > target markers menu. I will leave these here however because for future reference because there could be a use case where you want to bind a target marker to a spell cast.

### Star / Golden Star of Healing

I put this on my healer so I can see them while tanking. Makes it immediately obvious who is my healer with just a glance over my shoulder to make sure they’re staying clean. It also lets me see them through walls since you can see the icons through walls up to a certain distance. Another benefit is since I typically run with a small group of people who are all familiar with each other, I can change the healer on the fly. Sometimes our healer goes AFK for a minute and I can just toss the Star of Healing onto the backup healer in the group and we can keep pulling while the group’s healer is AFK. Once he’s back, quick press of the keyboard and he gets the star back and everybody knows what’s going on without having to say anything. Keeps the dungeon machine oiled.

```
/run SetRaidTarget("target",1)
```

### Orange Circle / Condom of Tanking Protection

While it’s obvious that the loud roaring 1200lb bear is the tank in a 5 man group, I still put the orange condom of protection over my head anyway. Main reason for this is these icons are visible through walls. I can disappear around a corner, tag a mob, and come back for LOS pulls and the group can see where I am through walls. Another small thing to keep the dungeon machine well oiled.

```
/run SetRaidTarget("target",2)
```

### Pink Diamond

```
/run SetRaidTarget("target",3)
```

### Green Triangle

```
/run SetRaidTarget("target",4)
```

### Moon

```
/run SetRaidTarget("target",5)
```

### Square

```
/run SetRaidTarget("target",6)
```

### X

```
/run SetRaidTarget("target",7)
```

### Skull

For the love of god focus DPS on this so we don’t have 3 DPS attacking 3 different targets. Mouth breathing DPS no longer have an excuse for pulling agro by attacking the wrong thing.

```
/run SetRaidTarget("target",8)
```

### Clear Icon from Target

```
/run SetRaidTarget("target",0)
```

Offensive Macros
----------------

### Faerie Fire

Faerie Fire and Feral Faerie Fire are separate spells. Yes, if you put this button on the primary button bar then you can put the right version of the spell on that bar for each form and it’ll just work. However, most of the key bars don’t change based on form. Using this macro instead of the direct spell allows you to put it onto a fixed bar. Cool thing is that by leaving #showtooltip without any spell afterwards, the macro is smart enough to display the tooltip of the spell it would cast based on your form. So you can even see the details of the version you’re about to use if you want.

This also allows you to cast Faerie Fire while you are in aquatic form, Travel Form, or are mounted. You can’t actually cast this spell from within these forms, but sometimes you wanna tag something **NOW** and you don’t want to lose time manually shifting out of these forms and then casting. Since /cancelform does not trigger a global cooldown, this macro is a single-press way to drop a faerie fire on the head of something while in these forms. The /dismount command does trip some kind of cooldown, but for some reason doesn’t share a cooldown with Faerie Fire so you can use this to drop a Faerie Fire on a target while you’re on a mount with a single keystroke. It’ll knock you off your mount, but you still get surgical strikes with your ranged pull.

```
#showtooltip
/dismount
/cast [stance:2] Aquatic Form; [stance:4] Travel Form
/cast [nostance] Faerie Fire; [stance:1] Faerie Fire (Feral); [stance:3] Faerie Fire (Feral)
```

### Attack Macros

Nothing too special here. This is an example for my Swipe macro, but this can be applied to any offensive attack. I bound /startattack to my swipe button so it’ll at least begin auto attacking even if I don’t have enough rage to swipe. Simple, but some people don’t know about this so I’m including this. I use the same thing for Bash, Shred, Swipe, Rake, etc… just create a new macro for each one and replace ‘swipe’ with the name of the attack.

```
#showtooltip
/startattack
/cast swipe
```

Support Spells
--------------

### Innervate

I spend most of my time tanking so I spend most of my time in bear form. Innervate has been a fantastic spell both in emergencies when the healer is OOM and we’re about to die, and when running a melee heavy group and the one caster in the group is low on mana and I don’t want to wait for him to drink. I’ve had two problems with it though – People sometimes don’t realize that I gave them innervate cuz they’re not paying attention, and I can’t cast it from bear form. This macro allows me to cast it immediately from within form, and it also sends a whisper to the target telling them they got Innervate and explains what that means.

```
#showtooltip
/cancelform
/run SendChatMessage("I just cast Innervate on you - 400% mana regen / 100% mana regen during casting next 20 seconds","WHISPER",nil,GetUnitName("target",1))
/cast innervate
```

These are what I got so far. I haven’t done anything with balance spells or healing macros. There’s a lot of potential there but I haven’t explored it yet. My focus has been on tanking and these are what I use on a daily basis. Hope these help soomebody. Like with all things coding and script related, there are going to be a lot of different ways of accomplishing any given macro. So these are just the ones I came up with, there are probably others out there that do the same thing differently. Great thing about the macro language in game is it pretty much allows you to set up your abilities however you want.

#### About the Author

![](https://www.warcrafttavern.com/wp-content/litespeed/avatar/681866ab246e66f4b25d384cdf326c4e.jpg?ver=1747684710)

#### Pippina