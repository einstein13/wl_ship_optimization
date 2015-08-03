======
Ship optimization in Widelands
======

Widelands project: https://wl.widelands.org/

Forum thread: https://wl.widelands.org/forum/topic/1762/

------

How to use this repository?

1. git https://github.com/einstein13/wl_ship_optimization.git (copy repository to your disc)
2. cd wl_ship_optimization (go to its folder)
3. python execute_all.py (to run all tests)
4. python execute_one.py (to run one test only)

To create your own class it is recommended:

1. To create ship class in new file in folder ships/
2. To add the class in settings.py SHIPS
3. To create port class in new file in folder ports/
4. To add the class in settings.py PORTS

------
Basic problem is to find best algorithm for ships transport in the game.
There are many ways to do that, but one of the easiest one is to make an experiment.

Algorithms here have the same rules as it is in Widelands:

* Ports and Ships are objects
* Those objects are separate and independet
* Both of them can contain wares

For "humans":

* settings.py is a file where all settings are defined
* it is recommended to add Port classes to folder ports
* it is recommended to add Ship classes to folder ships
* overriding any method is welcome in your class
* adding new methods is ok, but remember to name it differently than the others
* adding new properties/ variables is possible to your class

