# Overview

Something that will selectively inventory a file system and build clickable web page of interesting folders. 'Interesting' means there's a certain file in it with some metadata, but it's going to be intermingled with a whole bunch of the directories we don't care about.

`Some\where\deep\really\deep\SuperCol\.project.meta`:

    Project: Super Collider
    Owner: Heracles
    Date Initiated: 0500-12-02
    etc...

Possible index output (with links):

    Project: Super Collider, <Heracles>, Started: 0500-12-02
    Project: Super Zapper, <Zeus>, Started: 0502-10-02
    Project: Dumb Collider, <Heracles>, Started: 0503-01-05

Asking for help elsewhere:    
  * https://softwarerecs.stackexchange.com/questions/47412/
  * https://www.reddit.com/r/SomebodyMakeThis/comments/7hs1vy/

## Scripts

**envapplist.py** - by Jon Hourd, made this quick and dirty script to compile this list to save the effort of constantly browsing the directory structure there.  Baby steps towards a better future!

-----
2018-01-11

Trying `.ini` format and ConfigParser to start with.

Excel fields to migrate (\* important)

    Job Name*
    Old Map ID
    New Map ID
    Series ID
    Link*
    Description*
    Client*
    Resource
    SDR
    Application
    NOTES

New fields:

    MapID*
    Title*
    Subtitle
    Description*
    Client*
    Contacts*
    Authors*

Derived fields, but INI overrides derived value:

    Link
    
...

We want updating to work in both directions. Editing .ini file should update the master table, and editing table should update .ini.
...or is that just a bad idea? Why do I feel like it should go both ways?