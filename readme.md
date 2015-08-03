======
Ship optimization in Widelands
======

:Widelands project: https://wl.widelands.org/
:Forum thread: https://wl.widelands.org/forum/topic/1762/

------

How to use this repository?

1. git https://github.com/einstein13/wl_ship_optimization.git (copy repository to your disc)
2. cd wl_ship_optimization (go to its folder)
3. python execute_all.py (to run all tests)
4. python execute_one.py (to run one test only)

To create 

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

