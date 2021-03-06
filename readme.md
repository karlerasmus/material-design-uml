# material-design-uml

This is a sprite library for material icons for use in PlantUML diagrams.

Sprites generated from Material icons repository (https://fonts.google.com/icons)


## Use

Separate includes exist for each icon category
+ Action
+ Alert
+ AV
+ Communication
+ Content
+ Device
+ Editor
+ File
+ Hardware
+ Home
+ Image
+ Maps
+ Navigation
+ Notification
+ Places
+ Search
+ Social
+ Toggle

Sprite naming follows the convention {category}_{icon name} e.g. device_storage. Spaces are replaced by underscores. Reference the material icon library when searching for a sprite


Example use:
```
@startuml
!include https://raw.githubusercontent.com/karlerasmus/material-design-uml/master/dist/device_sprites.iuml

'Use sprite on component
Component "Storage component <$device_storage>"

@enduml
```
