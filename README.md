# Rymora-Land-of-Heroes
Game based on the RPG Rymora, Land of Heroes.

This game has two main packages: the core with all the logic and the graphics that makes calls to the core

## rymora API (core package)

The core contains all the game's logic. There are two main objects in the core: `Char` and `Item`
### Class `Char`
The `Char` class have all the attributes, properties and methods for controlling a character in the game, whether it's a playable character, a monster or anything that will `Attack` use `Skills` or `Equipment`. It inherits the `Base` class.
There's only one positional argument, the character's `name`. There are also three optargs: HP, SP, and ST. Since the arguments for creating this class are quite extensive, it's advised to use one of it's `classmethods` to instantiate it. This class uses `kwargs` in the following table plus the ones inherited from `base.Base`:

|kwargs| type | description|
|-----|------|------------|
| skills|`skills.Skills`| character's skills|
| Equipment| `equipment.Equipment`| character's equipment|

#### Char attributes
All arguments are available as attributes inside the instance. All the custom objects described in the table above have it's own API described here.
Extra attributes created are `self.maxHP`, `self.maxSP` and `self.maxST` which are either passed as optargs or calculated from the char's stats.

#### Char properties
`HP`, `SP` and `ST` are accessible as properties (inherited from `base.Base`). They have `getters` and `setters` as `self.HP`, `self.SP` and `self.ST`. Also accessible as a percentage: `self.HP_percent`, `self.SP_percent` and `self.ST_percent`, between 0 and 1
<!-- finish and list remaining properties -->

#### Char methods
* `calculate_stats():` - Calculates the stats (`HP`, `SP` and `ST`) and updates it's maximum value.
* `run_effects():` - Runs any effects in the `self.effects` list. Inherited from `base.Base`
* `attack(enemy, damage=True):` - Attacks the `enemy`. If `damage` is set to `False` the enemy is not damaged nor receives any `effects`, a tuple of (`damage`, `effects list`) is returned instead.

#### Char classmethods
* `blank(name, **kwargs):` - Creates a blank char with 0 in all stats and all the objects set. You can add data with `kwargs` the same way as the default class initializer.

#### Char inherited methods
Some methods are accessible through the characters attributes, their objects are described below.

### Class Item
<!-- Do the documentation -->

### Auxiliary classes
There are a series of auxiliary classes. They're not meant to be instantiated alone, but to create instances of either `Char` or `Item`. Their methods are available to any instance that uses them.
#### Class `base.Base`
This is the base class for creating `Char` and `Item` It has the following arguments:

|kwargs| type | description|
|-----|------|------------|
| lvl|`int`| character's level|
| attributes| `attributes.Attributes`| character's attributes|
| defenses| `defenses.Defenses`| character's defenses|
| resists| `resists.Resists`| character's resists|
| inventory| `inventory.Inventory`| character's inventory|
| effects| `dict` of `effects.Effects`, `keys` are the effects names| character's effects|
| powers| `dict` of `powers.Powers` `keys` are the powers names| character's powers|
| spells| `dict` of `spells.Spells` `keys` are the spells names| character's spells|
| bonuses| `dict` of `bonuses.Bonuses` `keys` are the bonus names| character's extra bonuses|

|optargs| type | description|
|-----|------|------------|
| HP| `int`| character's health points|
| SP| `int`| character's spiritual points|
| ST| `int`| character's stamina|

|posargs| type | description|
|-----|------|------------|
| name| `str`| character's name|
<!-- Describe better  -->

#### Class `attributes.Attributes`
This class manages the character's attributes. Arguments are:
* "strength": char strength
* "agility": char agility
* "vitality": char vitality
* "wisdom": char wisdom
* "inteligence": char inteligence
* "charisma": char charisma

each one of these attributes are accessible as attributes in the instance and have a property associated to them:
* `self.str_mod`: char strength modifier
* `self.agi_mod`: char agility modifier
* `self.vit_mod`: char vitality modifier
* `self.wis_mod`: char wisdom modifier
* `self.int_mod`: char inteligence modifier
* `self.cha_mod`: char charisma
<!--  Correct _mod names or attribute names for consistency-->

Also each one of the attributes have a method associated to them which returns the value for a test of the attribute
* `self.roll_str(bonus=None)`: Rolls a test of strength
* `self.roll_agi(bonus=None)`: Rolls a test of agility
* `self.roll_vit(bonus=None)`: Rolls a test of vitality
* `self.roll_wis(bonus=None)`: Rolls a test of wisdom
* `self.roll_int(bonus=None)`: Rolls a test of inteligence
* `self.roll_cha(bonus=None)`: Rolls a test of charisma - not implemented

<!--  Add roll method-->
## rymora_UI API (graphics package)
<!-- Do the documentation -->
