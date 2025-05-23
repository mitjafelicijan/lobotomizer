# Hunter Pet Macros for WoW Classic

* Author: [churchvibez](https://www.warcrafttavern.com/author/churchvibez/)
* Date: March 6, 2025
* Updated: March 8, 2025
* Expansion: [WoW Classic](/wow-classic/)

LnRiLWNvbnRhaW5lciAudGItY29udGFpbmVyLWlubmVye3dpZHRoOjEwMCU7bWFyZ2luOjAgYXV0b31AbWVkaWEgb25seSBzY3JlZW4gYW5kIChtYXgtd2lkdGg6IDc4MXB4KSB7IC50Yi1jb250YWluZXIgLnRiLWNvbnRhaW5lci1pbm5lcnt3aWR0aDoxMDAlO21hcmdpbjowIGF1dG99IH0gQG1lZGlhIG9ubHkgc2NyZWVuIGFuZCAobWF4LXdpZHRoOiA1OTlweCkgeyAudGItY29udGFpbmVyIC50Yi1jb250YWluZXItaW5uZXJ7d2lkdGg6MTAwJTttYXJnaW46MCBhdXRvfSB9IA==

### Contents

1. [Overview](#ftoc-overview)
   1. [Stances and Commands](#ftoc-stances-and-commands)
   2. [Abilities](#ftoc-abilities)
2. [Ability Ranks](#ftoc-ability-ranks)
3. [Basic Pet Macros](#ftoc-basic-pet-macros)
   1. [Feed Pet](#ftoc-feed-pet)
   2. [Feign Death](#ftoc-feign-death)
   3. [Pet Attack](#ftoc-pet-attack)
   4. [Pet Recall](#ftoc-pet-recall)
   5. [All-in-One Pet Management](#ftoc-all-in-one-pet-management)
4. [Advanced Pet Macros](#ftoc-advanced-pet-macros)
   1. [Mouseover Pet Attack](#ftoc-mouseover-pet-attack)
   2. [Feed Pet from Specific Bag Slot](#ftoc-feed-pet-from-specific-bag-slot)
   3. [Ability Toggling](#ftoc-ability-toggling)
   4. [Hardcore Defensive](#ftoc-hardcore-defensive)

Macros in Classic WoW extend beyond using player spells — they can also be used to manage your pet. As a Hunter, you can include pet abilities or stances in any macros along with your own abilities.

Proper pet management is crucial. The best Hunters tend to have excellent pet management and, for this, use advanced pet macros. These macros, however, can take time to get used to, and can cause issues if misused.

[![icon - beast mastery](https://www.warcrafttavern.com/wp-content/uploads/2022/07/ability_hunter_beasttaming.jpg)](https://www.warcrafttavern.com/wow-classic/guides/hunter-pets/)

[Hunter Pets Guide](https://www.warcrafttavern.com/wow-classic/guides/hunter-pets/)

[![wolf icon](https://www.warcrafttavern.com/wp-content/uploads/2025/02/wolf-icon.jpg)](https://www.warcrafttavern.com/wow-classic/guides/best-hunter-pets-for-dungeons-raiding-leveling-and-pvp/)

[Best Hunter Pets](https://www.warcrafttavern.com/wow-classic/guides/best-hunter-pets-for-dungeons-raiding-leveling-and-pvp/)

[![beast training icon](https://www.warcrafttavern.com/wp-content/uploads/2025/02/Beast-Training-Icon.jpg)](https://www.warcrafttavern.com/wow-classic/guides/how-to-train-your-hunter-pet/)

[Hunter Pet Training](https://www.warcrafttavern.com/wow-classic/guides/how-to-train-your-hunter-pet/)

[![world of warcraft addons & macros](https://www.warcrafttavern.com/wp-content/uploads/2021/04/World-of-Warcraft-Addons-Macros.jpg)](https://www.warcrafttavern.com/wow-classic/guides/hunter-pet-macros/)

[Hunter Pet Macros](https://www.warcrafttavern.com/wow-classic/guides/hunter-pet-macros/)

[![season of discovery hunter rune beast mastery](https://www.warcrafttavern.com/wp-content/uploads/2023/11/Season-of-Discovery-Hunter-Rune-Beast-Mastery.jpg)](https://www.warcrafttavern.com/wow-classic/guides/hunter-pet-abilities/)

[Hunter Pet Abilities](https://www.warcrafttavern.com/wow-classic/guides/hunter-pet-abilities/)

Overview
--------

Hunters usually keybind their pet’s abilities directly on the pet action bar, but there are some situations where it is better to include pet abilities or stances within macros instead.

One example of this is with [Feign Death](https://warcraftdb.com/classic/spell/5384). A Hunter should macro `/petpassive` into their [Feign Death](https://warcraftdb.com/classic/spell/5384) macro to prevent the pet from continuing to attack while feigning. This increases the chance of successfully dropping combat, because an attacking pet can cause this spell to bug and not get the Hunter out of combat.

Pet stances and abilities can all be written within macros as well as being keybound:

### Stances and Commands

```
/petattack
/petfollow
/petstay
/petpassive
/petdefensive
/petaggressive
```

### Abilities

```
/cast Growl(Rank 1)
/cast Dash(Rank 1)
/cast Claw(Rank 1)
```

Ability Ranks
-------------

Since early Season of Discovery, pet cast macros have been updated to require the rank to be specified when using an ability. If you do not specify the rank, the macro will not work.

Whenever you create pet macros with an ability, make sure to remember not only the correct format, but also the specific rank that you want to use.

Here are some examples to show how the syntax has changed:

Before:

```
/cast Growl
/cast Claw
/cast Dash
```

Now (changes in bold):

```
/cast Growl(Rank 5)
/cast Claw(Rank 8)
/cast Dash(Rank 3)
```

Basic Pet Macros
----------------

Below are some simple but handy pet macros that every Hunter should consider using.

### Feed Pet

```
/cast Feed Pet
/use Roasted Quail
```

This macro allows you to instantly [feed your pet](https://warcraftdb.com/classic/spell/6991) with one click, provided you have [Roasted Quail](https://warcraftdb.com/classic/item/8952) in your bags.

You can change out [Roasted Quail](https://warcraftdb.com/classic/item/8952) in the above example to any food your pet family can eat.

### Feign Death

```
/cast Feign Death
/stopattack
/stopcasting
/petpassive
```

This macro commands your pet to stop attacking when you cast [Feign Death](https://warcraftdb.com/classic/spell/5385). If your pet continues attacking the mob, there will be a higher chance that you will not drop combat when you feign.

Hunters often use this macro while raiding in combat if they want to swap trinkets. Having their pet passive as they [Feign Death](https://warcraftdb.com/classic/spell/5385) almost guarantees an instant combat drop, which makes trinket swapping work.

### Pet Attack

```
/petattack
```

It is recommended for every Hunter to have a separate bind for their pet attack.

A common mistake some Hunters do is binding /petattack into all abilities. This is generally not recommended, as there are situations where you may want to shoot a target but not send your pet in at the same time.

An example of this is **Baron Geddon’**s [Inferno](https://warcraftdb.com/classic/spell/19695) ability in [The Molten Core](https://warcraftdb.com/classic/zone/2717), where melee must move away while ranged continue to hit the boss – calling back your pet here will prevent it from dying.

### Pet Recall

```
/petpassive
/cast Dash(Rank 3)
```

This macro commands your pet to return to you while activating [Dash](https://warcraftdb.com/classic/spell/23110) (or [Dive](https://warcraftdb.com/classic/spell/23148), if you have a ![bat icon](https://www.warcrafttavern.com/wp-content/uploads/2025/02/bat-icon.jpg) **Bat**), which makes it come back to you quicker than usual.

This is useful if your pet is taking some form of damage and is about to die. Calling it back with increased movement speed can help it avoid taking an extra tick of damage.

### All-in-One Pet Management

Again, in the example below, you can change [Roasted Quail](https://warcraftdb.com/classic/item/8952) to whichever food you want to feed your pet with.

```
/cast [@pet,noexists,mod:shift] Call Pet
/cast [@pet,dead] Revive Pet
/cast [@pet,noexists,nomod] Revive Pet
/cast [@pet,nodead,mod:shift] Dismiss Pet
/cast [@pet,exists,nodead,nocombat] Feed Pet
/use [@pet,exists,nodead,nocombat] Roasted Quail
```

This is a well known macro which combines multiple pet management abilities into one. It performs different actions depending on your pet situation and whether you are holding down the Shift key or not.

* If your pet is not summoned, it will call your pet with [Call Pet](https://warcraftdb.com/classic/spell/883).
* If your pet is dead, it will revive your pet with [Revive Pet](https://warcraftdb.com/classic/spell/982).
* If your pet is alive, and you are holding down shift, it will dismiss your pet with [Dismiss Pet](https://warcraftdb.com/classic/spell/2641).
* If your pet is alive, and shift is not held, it will feed your pet [Roasted Quail](https://warcraftdb.com/classic/item/8952) with [Feed Pet](https://warcraftdb.com/classic/spell/6991).

In general, advanced Hunters do not use this macro as they have all of their pet management commands keybound on separate binds, rather than using modifier keys for the same bind, as this allows for better pet control.

Advanced Pet Macros
-------------------

The best Hunters keep their pets on passive at all times, which helps as it allows for complete pet control. Defensive and aggressive are almost never used except for specific situations. Keeping your pet on passive is necessary for some of the advanced macros to function correctly.

Keep in mind that some of these macros can take time to get used to, and misusing them can cause more harm than good.

### Mouseover Pet Attack

```
/petattack [@mouseover,harm,nodead][]
```

This macro allows you to send your pet on a new mob without you switching targets. If hovering over an enemy, the pet will attack that target; otherwise, it will attack your current target.

This is popular in many cases, one example of which is leveling. If you are attacking a low health mob, you can send your pet to another mob using mouseover without switching target yourself, meaning you finish off the mob while your pet builds aggro on the next mob.

Be mindful of where your cursor is when using this macro, as you may press it with your cursor hovering over an enemy you do not wish to attack.

### Feed Pet from Specific Bag Slot

```
#showtooltip 3 1
/cast [nocombat][pet] Feed Pet
/cast [nocombat][pet] 3 1
```

This was a popular macro used on older Blizzard clients when the standard [Feed Pet](https://warcraftdb.com/classic/spell/6991) macro did not function properly.

This macro feeds your pet using whatever is in the **third** bag from the left and in the **first** slot (hence the **3 1**).

If the slot is empty, the macro will not work, even if food exists elsewhere in your bags.

### Ability Toggling

These are very popular macros for leveling Hunters, used to toggle autocast on or off for specific abilities depending on their situation.

```
/petautocasttoggle Growl(Rank 3)
```

This will toggle [Growl](https://warcraftdb.com/classic/spell/14917) on or off, depending on its current state.

```
/petautocastoff Growl(Rank 3)
/petautocaston Claw(Rank 2)
/petautocaston Bite(Rank 3)
```

This is a popular example of a macro used when you are kiting a mob which your pet cannot tank because it will die to it easily. You should have full aggro on the mob, and your pet will follow and hit the mob with [Claw](https://warcraftdb.com/classic/spell/3010) and [Bite](https://warcraftdb.com/classic/spell/17268) while not using [Growl](https://warcraftdb.com/classic/spell/14920) to avoid climbing further up the threat table.

A good example of this is kiting [Chieftain Nek’rosh](https://warcraftdb.com/classic/npc/2091) in [Wetlands](https://warcraftdb.com/classic/zone/11) for the quest ![Wow Alliance Crest](https://www.warcrafttavern.com/wp-content/uploads/2021/01/WoW-Alliance-Crest.png) [Defeat Nek’rosh](https://warcraftdb.com/classic/quest/474) while leveling. Hunters can solo this, but many other classes cannot and must look for a group.

Remember, you need to specify ability ranks for this macro to work!

### Hardcore Defensive

```
/cast Arcane Shot
/petdefensive
```

In Hardcore, this macro ensures that if the player disconnects, the pet will continue to fight mobs while the Hunter is not in the game, which can end up saving the Hunter’s life. You can replace [Arcane Shot](https://warcraftdb.com/classic/spell/3044) with any ability you commonly use.

Defensive should be used with caution and practice, as it will result in the loss of some pet control in exchange for covering a potential survival risk.

#### About the Author

![](https://www.warcrafttavern.com/wp-content/uploads/tml-avatars/cv3.jpg)

#### churchvibez

I've been playing Classic World of Warcraft at the highest level for many years, taking part in world first raiding, speedrunning, and occasionally speedleveling through newly released content.