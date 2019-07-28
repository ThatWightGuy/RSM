# Resume Standardization Markup (RSM)

RSM is a limited Markup Language that aims to simplify the process of creating and analyzing resumes

## Tags

```<res></res>``` ==> body tag, creates the body of an RSM file

```<page><page>``` ==> denotes a new page in the resume

```<info><info>``` ==> denotes a new block of information

  * info tags have default types (denoted by ```type = ' '```)
  * Default types:
    - 'sum' : summary
    - 'edu' : education
    - 'emp' : employment history
    - 'skills': skills
    - 'certs': certification
    - 'proj' : projects
    
```<header></header>``` ==>  denotes a block of header information
  * will have a parameter "legacy" which will be a boolean denoting if the header should be copied
  
```<link></link>``` ==> denotes a link to a website
  * will have a parameter "type" denoted by ```type = ' '```
    - Types:
      + "linkedin"
      + "email"
      + "github"
      + "website"
      
```<blk></blk>``` ==> generic block tag used for separating things within named tags.  Ignored by interpreter

## Internal Tags

```<item></item>``` ==> denotes item inside ```<info>```
  * "type" variables for ```<item>```:
    - "text" : denotes plaintext
    - "list" : can be used in conjuction with ```<ib>```
    - "skill" : a possible attribute that will be used to denote skills within "skill" attributes in ```<info>``` tag.  
    Might just be replaced with ```<ib>```
    Might have additional optional supplementary attribute "level" which will denote skill level ranging from 1-5
    - "block" : default attribute (does not need to be set).  Denotes ```<item>``` as block set of info will be interpreted by the ```<info>``` attribute

```<it></it>``` ==> item title, title of whatever piece of info the ```<item>``` is.  Example: Job Title

```<ib></ib>``` ==> bullet point description for ```<it>``` 

```<idates></idates>``` ==> denotes block of date info
  * ```<start></start>```, ```<end></end>``` : for a timeframe
  * ```<date>,</date>``` : for a singular date
    - will have attributes "m = ", "d = ", "y = "
    
```<hname></hname>``` ==> person's name

```<loc></loc>``` ==> contains information relating to an address using the following internal tags:
  * ```<addr1></addr1>``` : address line 1
  * ```<addr2></addr2>``` : address line 2
  * ```<city></city>``` : city associated with address
  * ```<spr></spr>``` : state/province/region
  * ```<zipp></zipp>``` : zip/postal code
  * ```<country></country>``` : country associated with address
  
```<hphone></hphone>``` ==> block of information regarding phone numbers
  * will have parameter for phone type denoted by ```type = ' '```
    - Types:
      + "home"
      + "work"
      + "cell"
  * will also have parameter "cc" denoting country code of the phone number
  
## ```<info>``` specific tags:

```<sum></sum>``` ==> summary text for that item, in this case, acts as a description of job activities.  
can be used in conjunction with ```<li>```.  can be used for all ```<item>```.

```<role></role>``` ==> optional tag used to denote a role at a company (ex: CEO).  used inside ```<item>``` tags whose parent
```<info>``` has type "emp".

```<deg></deg>``` ==> block tag for degrees and has the following internal tags:
  * ```<dtype></dtype>``` : degree type
  * ```<dsub></dsub>``` : subject
