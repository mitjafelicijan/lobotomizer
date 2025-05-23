# Feral Druid DPS Powershifting Rotation Guide – WoW Classic

* Author: [Oxykitten](https://www.warcrafttavern.com/author/oxykitten/)
* Date: November 15, 2021
* Updated: July 28, 2024
* Expansion: [WoW Classic](/wow-classic/)

### Contents

1. [Energy & Global Cooldown](#ftoc-energy-global-cooldown)
2. [Powershifting](#ftoc-powershifting)
3. [Powershift Rotation and ‘Cycles’](#ftoc-powershift-rotation-and-cycles)
4. [Cast Priorities](#ftoc-cast-priorities)
5. [‘Leeway’ (advanced)](#ftoc-leeway-advanced)
6. [Mana Management](#ftoc-mana-management)
7. [Conclusion](#ftoc-conclusion)

The purpose of this guide is to summarise important information on the [Feral Druid DPS](https://www.warcrafttavern.com/wow-classic/guides/feral-druid-pve-dps/) rotation in WoW Classic. It will cover what powershifting is, how to do it and how we maximise our DPS. For more information on other aspects of playing a feral druid.

Energy & Global Cooldown
------------------------

The most important resource to consider for a feral DPS is energy. We have 100 energy, which regenerates in discrete ticks of 20 energy every 2 seconds. Our main abilities cost between 30 and 48 energy. In cat form, our global cooldown (GCD, the time period after casting a spell in which no other spells can be cast) is 1 second. In caster form (and when shifting into any form), our GCD is 1.5 seconds – this will be relevant later on. This means that if we stay in cat form, the rate limiting factor in our rotation – that is, what we need to wait for in order to cast our abilities – is energy, as our GCD allows us to spend energy much faster than we regenerate it.

Shifting into or out of cat form does not impact our energy ticks – they continue to tick every 2 seconds, meaning if we leave cat form 1 second after our energy tick and immediately re-enter cat form, we will still receive our next energy tick after 1 more second.

Powershifting
-------------

Powershifting is the basis of the feral DPS rotation in Classic WoW. It is possible because of the resto talent, [Furor](https://wowclassicdb.com/spell/17061), which awards 40 energy when entering cat form, and the level 40 crafted helmet, [Wolfshead Helm](https://wowclassicdb.com/item/8345), which awards 20 energy when entering cat form. Together, these give the druid 60 energy when entering cat form. Therefore, after expending all our energy, we are able to exit cat form (which does **not** start a GCD) and re-enter it immediately, ‘resetting’ our energy to 60 with the click of a button. We call this powershifting, and it is easily done in Classic with a simple macro:  
  
*#showtooltip  
/cast [form:3] Cat Form  
/cast Cat Form*

Powershifting gives us the energy to cast abilities at a much faster pace; specifically, we are able to cast 2 abilities every 4 seconds, as opposed to every 8 seconds without, massively increasing our DPS and allowing us to be relatively competitive with other classes on a single target.

This of course means that the Furor talent is absolutely mandatory, and [Wolfshead Helm](https://wowclassicdb.com/item/8345) is the best helm in the game in all phases of content for a feral DPS. By casting abilities more often, [Wolfshead Helm](https://wowclassicdb.com/item/8345) scales with how strong your abilities are – this means that the more stats you get from all your other gear, the stronger Wolfshead gets, and no other helm can come close.

Because powershifting allows us to get energy on command, **energy is not the rate limiting factor in the feral rotation (for the most part). Instead, we maximise our use of GCDs to cast as many abilities as possible.**

Powershift Rotation and ‘Cycles’
--------------------------------

We describe our rotation of powershifting and casting abilities in terms of 4 second ‘cycles,’ where, generally, we:

*Powershift (bringing you to 60 energy – energy tick thereafter brings you to 80)  
Shred (bringing you to 32 energy – energy tick then brings you to 52)  
Shred or Bite (Bringing you to 4 or 0 energy)  
Powershift (Bringing you back to 60 energy and restarting the cycle)*

Continuously in blocks (‘cycles’) of 4 seconds. The diagram below illustrates these cycles, showing our casts in blue, the GCD in red following casts, and energy ticks in yellow throughout.

[![pve feral druid powershifting cycle](https://www.warcrafttavern.com/wp-content/uploads/2021/11/image-1.png)](https://www.warcrafttavern.com/wp-content/uploads/2021/11/image-1.png)

As seen in the diagram above, each cycle starts with a powershift 1 second into an energy tick. This starts a 1.5 second (caster) GCD, during which we get an energy tick to bring us to 80 energy. We then cast an ability as soon as the GCD ends. Here, we wait for the next energy tick (0.5 seconds after the GCD ends) so that we can cast a second ability. Once the 1 second GCD ends, we immediately powershift. While we do wait for energy in the middle of this cycle, what is essential in maximising your overall DPS is to **time your powershift at the end of the cycle as soon as your GCD has ended and you are able to shift –** the focus is *not* on the energy tick, which will line up correctly in your next cycle if you have shifted as soon as possible.

**Cast Priorities**
-------------------

In Classic, knowing which ability to cast within those cycles is fairly simple, as there are very few worthwhile abilities for a feral dps. The rotation can be portrayed as a cast priority order as shown below:

1. *≥30 energy, 5 combo points, Rip debuff is not on the target:* ***[Rip](https://wowclassicdb.com/spell/9896)\****
2. 35-62 energy, ≥4 combo points: [**Ferocious Bite**](https://wowclassicdb.com/spell/22829)
3. ≥48 energy: **[Shred](https://wowclassicdb.com/spell/9830)**
4. *40-47 energy, >1 second away from energy tick:* ***[Claw](https://wowclassicdb.com/spell/9850)\*\****
5. ≤20 energy away from next ability and ≤1 second away from tick: **Wait for energy**
6. ≤20 energy away from next ability and >1 second away from tick: **Powershift**
7. >20 energy away from next ability: **Powershift**

*\*This step is optional; using only Ferocious Bite instead of Rip is approximately equal DPS to using both.*  
*\*\*This step is niche and optional; using claw at the right time is a small DPS gain, but difficult to execute and is not needed often. Using claw at the* ***wrong*** *time, however, is a significant DPS loss.*

In fact, the lists above works as a flowchart for the entire feral rotation. However, I feel getting into the rhythm and muscle memory of a cyclical pattern is easier to learn.  
  
**Assuming a “Shift, Cast, Cast, Shift” cycle as described in previous sections, your cast priorities (i.e. which ability you use in a “cast”) can be easily summarised as:**

1. Use combo points on Rip or Ferocious Bite if you have them
2. Use shred

**Note that you should not use Ferocious Bite when over 62 energy**, as it drains all of your energy for very little damage gain. Instead, if over 62 energy you should shred (even if at 5 combo points) and then Ferocious Bite on the next energy tick (assuming the Rip debuff is already up, or you are using a Bite-only rotation).

**Also note that your uptime on the boss does *not* affect which finisher you should use.** It is a common misconception that if you are about to lose uptime on a boss (e.g. Onyxia about to fly away) you should use Rip instead of Ferocious Bite as the damage will continue to tick while you are not attacking the boss. However, if Rip does 1000 damage over 12 seconds and Ferocious Bite does 1000 damage instantly, the end result is exactly the same DPS. The exception to this is if a boss is about to die, or if they are about to enter an *invulnerability phase* where they are immune to damage. In these cases, Ferocious Bite is better as Rip does not have time to deal its full damage.

**‘Leeway’ (advanced)**
-----------------------

Looking at the diagram in the ‘Powershift rotation and cycles’ section, you may notice that there is a 0.5 second period where we are not under GCD, while waiting for an energy tick. There are certain scenarios in which we are able to take advantage of this gap by fitting an extra ability into our cycle at no extra cost to increase our DPS. We refer to this as ‘leeway.’ There are three main scenarios where leeway is relevant:

*Applying [Faerie Fire](https://wowclassicdb.com/spell/17397) (if you are the only druid in a group)  
Having your first cast in a cycle miss, or be dodged  
Getting an [Omen of Clarity](https://wowclassicdb.com/spell/16864) proc early in your cycle*

[Faerie Fire](https://wowclassicdb.com/spell/17397) and abilities cast with [Clearcasting](https://wowclassicdb.com/spell/16870)  up (the Omen of Clarity proc) do not use any energy, and can therefore be cast while waiting for the energy tick. When you miss a combo-point generating ability, you get 80% of the energy cost refunded to you, which in practice can allow you to cast the ability again without waiting for an energy tick. Here, you may notice that the GCD gap in a 4 second cycle is 0.5 seconds long, but an ability starts a 1 second GCD, delaying your cycle. However, leeway uses the 0.5 second gap from the current cycle as well as the *following cycle*, meaning that over time there is no delay. This is illustrated in the diagram below, showing two consecutive cycles in which leeway is used to cast Faerie Fire:

[![pve feral druid powershifting  cycles](https://www.warcrafttavern.com/wp-content/uploads/2021/11/image-2.png)](https://www.warcrafttavern.com/wp-content/uploads/2021/11/image-2.png)

In this diagram we can see that while the first cycle is delayed to 4.5 seconds by casting Faerie Fire, the following cycle is shortened to 3.5 seconds and over both, there is no delay. Importantly, the shift happens at 4.5 seconds, and the energy tick comes in at 5 seconds – this is what makes the 3.5 second rotation possible, as further delay in the previous cycle could cause you to “miss the tick,” leaving you without enough energy to cast 2 abilities and therefore delay the next cycle by *up to 2 seconds.*

Leeway means that in our rotation, misses are not always punishing – their damage loss can often be ‘recovered.’ Note that finishing moves (Rip and Ferocious Bite) **do not refund energy on misses.** If you miss on the **second** cast in your cycle, you can cast the ability again afterwards but it **will** delay your cycle. For maximum DPS, you should cast your ability only if you have enough energy to do so, or will have enough energy to do so with an energy tick **less than one second away.** Otherwise, you should powershift to not delay your following cycle. Finally, if you get an Omen of Clarity proc *after* your second cast in the cycle, make sure you powershift and then use the leeway in your *next* cycle instead of delaying your current cycle.

**Mana Management**
-------------------

As you can imagine, shifting in and out of cat form every 4 seconds costs a lot of mana, and in feral gear, we do not have very much mana. This makes feral DPS one of the most mana-intensive rotations in the game. Because of this, it is essential to use as many mana potions ([Major Mana Potions](https://wowclassicdb.com/item/13444) restore **1350-2250 mana** on a 2 minute cooldown) and [Demonic Runes](https://wowclassicdb.com/item/12662) or [Dark Runes](https://wowclassicdb.com/item/20520) (**900-1500 mana** on a 2 minute cooldown) as possible during boss fights. More specifically:

1. As soon as you have used 1500 mana, use a Demonic/dark rune
2. As soon as you have used 2250 more mana, use a Major Mana Potion
3. Continue using these on cooldown

You may use these consumables *within* a powershift with separate macros for each. Make sure to use them at the end of a cycle, when you would powershift anyway, to not lose any DPS.

*#showtooltip  
/cast [form:3] Cat Form  
/use Major Mana Potion  
/cast Cat Form*

#*showtooltip  
/cast [form:3] Cat Form  
/use Demonic Rune  
/cast Cat Form*

Asking your paladins to keep [Judgement of Wisdom](https://wowclassicdb.com/spell/20357) up on the boss makes a massive difference as well **(Judgement of Wisdom generates more mana than potions and runes put together),** and use your [Innervate](https://wowclassicdb.com/spell/29166) on yourself (ideally before combat starts so you don’t lose DPS by casting it) as an offensive cooldown. **With the long fights expected in Season of Mastery, mana will be a serious struggle for Feral DPS. This means that playing Alliance for Judgement of Wisdom will be far better than playing Horde.** If you’re struggling with mana despite all this, the trinket [Rune of Metamorphosis](https://wowclassicdb.com/item/19340) from [Blackwing Lair](https://www.warcrafttavern.com/wow-classic/guides/bwl/) can be very strong.

**Conclusion**
--------------

Feral DPS uses its powershifting rotation to maximise GCD use rather than waiting for energy regeneration. This allows us to massively increase our DPS and be somewhat competitive with other classes. While it may seem complex and difficult to master, getting into the “shift, cast, cast, shift” rhythm just takes a bit of practice, after which you’ll be able to brag to your frostbolting mages about your engaging playstyle. To help you in-game, I recommend using WeakAuras such as Weave’s Feral Bar, along with any obvious GCD indicator WeakAura – I’ve linked my labelled UI in an image below (and I know, it’s a mess). I hope this guide was useful; feel free to leave a comment, or find me as Oxy on the [Druid Classic discord server.](https://discord.gg/SMwmrBV)

[![pve feral druid powershifting ](https://www.warcrafttavern.com/wp-content/uploads/2021/11/Screenshot-9_LI-1024x576.jpg)](https://www.warcrafttavern.com/wp-content/uploads/2021/11/Screenshot-9_LI.jpg)

#### About the Author

![](https://www.warcrafttavern.com/wp-content/litespeed/avatar/96f5b2803c0a91aac3733e7ccf3c51f1.jpg?ver=1747873045)

#### Oxykitten

I've been an avid WoW player since Vanilla. At 6 years old, I was slowly progressing through Blackfathom Deeps and levelling up with my brothers. Since Classic Wow launched, I've found a new way to enjoy the game; participating in Feral Druid theorycrafting communities and performing well in an underdog class has been a fun challenge. I hope to be able to share all I've learned with anyone who shares that interest!