# Overview

Something that will selectively inventory a file system and build clickable web page or some othe UI of interesting folders. 'Interesting' means there's a certain file in it with some metadata, but it's going to be intermingled with a whole bunch of the directories we don't care about.

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
2017-12-22

Minimum info:

    Title/Name
    Summary/tag line/purpose
    Authors
    Intitiation date
    Latest milestone/release/published date
    Clients

Nice to have:

    Thumbnail
    Extended description
    (Status?)
    Related projects
    Tags

### Index interface

Speed tiles/dial (grid or list)
Sort & filter by any attribute
Find-as-you-type: 
 - for all fields, or
 - just that field if in/above/below column
Clickable - opens the folder on disk

### Method
Marker file in the interesting folder, plain text of at least the minimum elements. Format? Markdown/YAML/INI/...

A scheduled crawler locates the marker files and adds them to the index

### Questions

* is the index a static page, like index.html or an app? (perhaps like Fossil SCM)
* is marker a single file? or folder? or a packaged file?
    * `zinfo.ini`
    * `zinfo/*.*`
    * `Project.zinfo`

## Why
Only some folders of the thousands are Interesting or Projects. The can be located anywhere. We often don't know ahead of time if a thing will be interesting. They start small.

ENV.499 folders and the Map-Index.xls are too big to understand now. The system is very useful and has saved our bacon countless times, but it's collapsing under it's own weight. 

### The Name
Amazingly the name **zinfo** is not widely used. I found 

- a polish website, http://zinfo.pl,  
- a Google Apps series by _[Zinfo Enterprises](https://play.google.com/store/apps/details?id=com.zinfoghoti.admin&hl=en)_ in India, which seems to be very lightly used. (It's a location based search and meta-info app for local info. Cool idea.) 
- Fashion watches for men
- 11 repositories on Github, only 1 of which has any significant activity or code and it's completely unrelated (https://github.com/ZRiemann/ZInfoTech)

**`Z`** - to sort to bottom of file explorer window in most instances. I'd rather not rely on hidden files because updating meta-data outside a management tool needs to be quick and easy, and approachable for less technical people. 

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

Better: table is only read only, but has [edit this project] action button.