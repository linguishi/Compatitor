### 竞争APP识别

#### 语料

清洗前`data/RawData.json`

清洗后`data/filterByLang.json`

接近 25000 个APP的描述信息。

document格式, 以*Dr. Cleaner*为例
```json
{
    "Appid": 921458519, 
    "AppName": "Dr. Cleaner: Disk, Memory, Cache and System Clean Tool",
    "Description": "Thanks to our users, Dr. Cleaner is the #1 free Mac cleaning App around the world! It is the ONLY free App that offers Memory Optimization, Disk Cleaning and Big Files Scanner to help you free your hard disk and speed up your Mac. NOW, Dr. Cleaner proudly introduces its new feature — Duplicate Finder!

Stop occupying your space with meaningless copies of files. With just one click from you, Duplicate Finder finds all duplicate files on your hard disk. It quickly scans your disk and clearly presents all the duplicates before you selectively choose which to delete.

Duplicate Finder is a paid feature, however, the trial will allow you to see how much your Mac is occupied by duplicate files. TRY it before you BUY it! 

USER COMMENTS
“It removes unwanted and useless files to clean up your mac. It does everything the description says.” — Kamil.D from Australia

“Very simple - very effective. Easy to use and great way to keep your Mac optimised.” — Damo1193 from U.K.

“Simply the best App I have ever used…” — Jani from Germany

PRIMARY FEATURES

[Smart Memory Optimizer]
• 1-click memory optimization
• Instantly reclaim memory from closed Apps
• Identify Apps that use a significant amount of memory
• Show real-time memory usage on status bar

[Junk Files Cleaner]
• Quick disk clean from status bar menu
• Clean temporary files, incl. logs, mail caches, iTunes and iOS temporary files, etc.Empty Trash for current user
• Clever detection of remaining files after deleting Apps

[Big Files Scanner]
• 1-click scan of big files (costomizable size from 100 MB and above)
Multiple filters of size, date, name and type
• Local files in sync with your cloud drives can also be found
• Protected files* will not be deleted
[* Important big files can be “locked” into the protected list to avoid false deletion.]

[Duplicate Finder]
• Thorough and selective scan — it has the fast and accurate scanning technique that covers every corner of your Mac. You can choose to scan your entire home folder or some specific folder(s).
• Smart and accurate selection — duplicates are selected not only by file names but also by their contents. Files are shown in detailed previews. it can also help you “decide” which copy to delete by presenting “Auto Select” button.
• Easy and safe decision — duplicates can be sorted by file type and listed in their full route for you to track. They can either be put in to Trash or deleted permanently according to your own decision.

We value your feedback! Please comment in the App Store or submit ideas and requests directly to our developers through our support portal (http://Appletuner.trendmicro.com/support). 
You can also email us directly at mac_support@trendmicro.com."
}

```

#### 训练
`trainModel.py` 

模型保存在 `data`文件夹中

#### 查询
`queryInterface.py`

`queryByAppid` 根据APPID查询
`queryByDescription` 根据英文描述查询

示例
```python
queryByAppid("921458519",5)
```
输出 **TOP5**

1. 
```json
{
    "Appid": 921458519, 
    "AppName": "Dr. Cleaner: Disk, Memory, Cache and System Clean Tool",
    "Description": "Thanks to our users, Dr. Cleaner is the #1 free Mac cleaning App around the world! It is the ONLY free App that offers Memory Optimization, Disk Cleaning and Big Files Scanner to help you free your hard disk and speed up your Mac. NOW, Dr. Cleaner proudly introduces its new feature — Duplicate Finder!

Stop occupying your space with meaningless copies of files. With just one click from you, Duplicate Finder finds all duplicate files on your hard disk. It quickly scans your disk and clearly presents all the duplicates before you selectively choose which to delete.

Duplicate Finder is a paid feature, however, the trial will allow you to see how much your Mac is occupied by duplicate files. TRY it before you BUY it! 

USER COMMENTS
“It removes unwanted and useless files to clean up your mac. It does everything the description says.” — Kamil.D from Australia

“Very simple - very effective. Easy to use and great way to keep your Mac optimised.” — Damo1193 from U.K.

“Simply the best App I have ever used…” — Jani from Germany

PRIMARY FEATURES

[Smart Memory Optimizer]
• 1-click memory optimization
• Instantly reclaim memory from closed Apps
• Identify Apps that use a significant amount of memory
• Show real-time memory usage on status bar

[Junk Files Cleaner]
• Quick disk clean from status bar menu
• Clean temporary files, incl. logs, mail caches, iTunes and iOS temporary files, etc.Empty Trash for current user
• Clever detection of remaining files after deleting Apps

[Big Files Scanner]
• 1-click scan of big files (costomizable size from 100 MB and above)
Multiple filters of size, date, name and type
• Local files in sync with your cloud drives can also be found
• Protected files* will not be deleted
[* Important big files can be “locked” into the protected list to avoid false deletion.]

[Duplicate Finder]
• Thorough and selective scan — it has the fast and accurate scanning technique that covers every corner of your Mac. You can choose to scan your entire home folder or some specific folder(s).
• Smart and accurate selection — duplicates are selected not only by file names but also by their contents. Files are shown in detailed previews. it can also help you “decide” which copy to delete by presenting “Auto Select” button.
• Easy and safe decision — duplicates can be sorted by file type and listed in their full route for you to track. They can either be put in to Trash or deleted permanently according to your own decision.

We value your feedback! Please comment in the App Store or submit ideas and requests directly to our developers through our support portal (http://Appletuner.trendmicro.com/support). 
You can also email us directly at mac_support@trendmicro.com."
}
```
2. 
```json
{
    "Appid": 1031826818, 
    "AppName": "Duplicate Finder - Retrieve and Remove Duplicate Files", 
    "Description": "Stop cluttering your disk space with meaningless copies of files. With just one click, Duplicate Finder finds all duplicate files on your hard disk. It quickly scans your disk and clearly presents all the duplicates so you can selectively choose which to delete.

Duplicate Finder is brought to you by the same team that created Dr. Cleaner. It features an easy-to-use drag and drop user interface and includes the following functions to keep your disk clean and organized:

• Thorough and selective scan — utilizes a fast and accurate scanning technique that scans your entire Mac. You can choose to scan your entire home folder or some specific folder(s).

• Smart and accurate selection — duplicate files are selected not only by file names, but also by their contents. Files are shown in detailed previews. You can also choose the \"Auto Select\" feature that recommends which copy to delete.

• Easy and safe decision — duplicates can be sorted by file type and listed with their full path for you to track to the original location. You can decide if they should be sent to Trash or permanently deleted.

We value your feedback! Please comment in the App Store or submit ideas and requests directly to our developers through our support portal:

http://Appletuner.trendmicro.com/forum/viewforum.php?f=8). 

You can also email us directly at:
mac_support@trendmicro.com."
}
```
3. 
```json
{
    "Appid": 989642619, 
    "AppName": "Clean Duplicate File", 
    "Description": "Boost up Memory, Clean and Optimize Disk - ALL in ONE – Supports 30 languages
“Powerful and more features integrated in single app. I’ll introduce family and friends to use” – William Adams.
“For just $10, your Mac will be brought to another level” – A Satisfied Customer.
“I have sent feedback that can make Clean Duplicate File even better. Please check” - Alan Moore.

Macs are used DAILY for INTENSIVE usage like editing, programming, and much more! Having TOO MANY apps open can DAMAGE or SLOW down your disk! That’s why you need to BUY our app, and EXTEND the life of your Mac!

Fast and Powerful CPU, RAM, Disk, File cleaner. Ranked in the TOP Paid App in 20 countries.

NEW featuring Boost up Memory, Optimize Disk, bring your Mac’s performance up to speed with these fantastic new features!

Clean Duplicate File performs a comprehensive sweep for junk files that are often left over after apps are uninstalled.

Clean Duplicate File automatically reclaims system memory when you close a memory-intensive app, INCREASING the productivity of your Mac!

~PRIMARY FEATURES~

*** BOOST up Memory ***
+ Automatically optimizes memory when apps close
+ Reclaim unused memory to make it available for use by other apps
+ Optimize memory with one click
+ Graph monitor to track real-time memory status

*** OPTOMIZE Disk ***
+ Clean temporary file such as logs, caches files, downloads, etc.
+ Empty current user’s Trash Can
+ Remind users to clean their disk when necessary

*** Find DUPLICATE Files ***
+ Files compared via our advanced SHA-1 hash checksum algorithm
+ Super fast and accurate duplicate detection
+ Locate duplicate images, audio, archives, entire folders and more
+ Automatic one-click duplicate selection

*** Find UNUSED & OLD Files ***
+ Add multiple folders for scanning
+ More condition with Size & Date
+ Automatic one-click scan

[WHY should you buy from us?]
Because we’ve worked hard to make Clean Duplicate File as simple and efficient as possible for you to use. There are many cleaner apps on the market, but ours WORKS, is SIMPLE to use, and MAXIMIZES your Mac’s performance! And we would love to hear your thoughts, just provide us with your feedbacks!"
}
```
4. 
```json
{
    "Appid": 989642623, 
    "AppName": "Duplicate Booster: Memory, Disk, File", 
    "Description": "Boost up Memory, Clean and Optimize Disk - ALL in ONE – Supports 30 languages
“Powerful and more features integrated in single app. I’ll introduce family and friends to use” – William Adams.
“For just $10, your Mac will be brought to another level” – A Satisfied Customer.
“I have sent feedback that can make Duplicate Booster even better. Please check” - Alan Moore.

Macs are used DAILY for INTENSIVE usage like editing, programming, and much more! Having TOO MANY apps open can DAMAGE or SLOW down your disk! That’s why you need to BUY our app, and EXTEND the life of your Mac!

Fast and Powerful CPU, RAM, Disk, File cleaner. Ranked in the TOP Paid App in 20 countries.

NEW featuring Boost up Memory, Optimize Disk, bring your Mac’s performance up to speed with these fantastic new features!

Duplicate Booster performs a comprehensive sweep for junk files that are often left over after apps are uninstalled.

Duplicate Booster automatically reclaims system memory when you close a memory-intensive app, INCREASING the productivity of your Mac!

~PRIMARY FEATURES~

*** Find DUPLICATE Files ***
+ Files compared via our advanced SHA-1 hash checksum algorithm
+ Super fast and accurate duplicate detection
+ Locate duplicate images, audio, archives, entire folders and more
+ Automatic one-click duplicate selection

*** OPTOMIZE Disk ***
+ Clean temporary file such as logs, caches files, downloads, etc.
+ Empty current user’s Trash Can
+ Remind users to clean their disk when necessary

*** BOOST up Memory ***
+ Automatically optimizes memory when apps close
+ Reclaim unused memory to make it available for use by other apps
+ Optimize memory with one click
+ Graph monitor to track real-time memory status

*** Find UNUSED & OLD Files ***
+ Add multiple folders for scanning
+ More condition with Size & Date
+ Automatic one-click scan

[WHY should you buy from us?]
Because we’ve worked hard to make Duplicate Booster as simple and efficient as possible for you to use. There are many cleaner apps on the market, but ours WORKS, is SIMPLE to use, and MAXIMIZES your Mac’s performance! And we would love to hear your thoughts, just provide us with your feedbacks!"
}
```
5.
```json
{
    "Appid": 1012324495,
    "AppName": "Duplicates Cleaner",
    "Description": "The best and the most splendid App on Mac App Store for cleaning duplicates on Mac!!  

Messed up with too many files on your Mac? Running short of hard disk space? 

The solution is here… Duplicates Cleaner finds all the duplicate files and helps you clean them to recover the lost disk space on your Mac. Very quick & easy-to-use and saves you tons of disk space.

Admirably Simple
Simply drag and drop a folder of your choice into Duplicates Cleaner to scan for duplicates and click Multi Select to quickly clean all the scanned duplicates.

Magnificently Fast
It takes Duplicates Cleaner only a few seconds to clean all the duplicates from your internal and external drives, irrespective of the number of files you have on your drives.

Remarkably Intelligent
Scans and finds all the duplicate and identical files on your Mac. It categorizes all the scanned files and makes sure that at least one copy of each file is kept unchanged.

Why you would love Duplicates Cleaner:
- Smart Scanning Algorithm: It quickly and smartly scans for all the duplicates and makes sure that the original remains intact. 
-  Splendid Navigation: It lets you easily navigate the duplicate files and have a look into the details of each of them before taking any action.
- One Click Multi Select: It lets you quickly select multiple files in just a single click making it simple to use.
- Elegant Design: It is beautifully designed. Its spectacular design lets you swiftly scan and preview files, which makes selection & cleaning of duplicates easy.

Why should you give it a try?
Eliminates Redundancy: 
- Scans all your drives for duplicate files and lets you clean them rapidly, thereby getting rid of all the redundant files on your Mac to save ample of disk space.
Recovers Disk Space: 
- After careful selection, it lets you clean all the duplicate files including photos, videos, music and much more to help you regain the lost but recoverable disk space on your Mac.
Organizes Scattered Files: 
- After cleaning the selected duplicate files, it lets you organize and manage all your remaining files at one place.
Cleans External Drives: 
- It not only scans your hard disk but also lets you scan and clean the duplicates on your external drives as well, irrespective of the number of files on the drive.

Get rid of all the duplicates and recover the valuable disk space on your Mac with Duplicates Cleaner now."
}
```

### Have Fun !!!