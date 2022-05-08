# atlas_debomifier

For some reason, **Adobe Animate** tends to encode it's texture atlas files with **UTF-8-BOM** which is stupid and tends to cause crashes when parsing.

So I made this ~~useful~~ tool to encode them in the regular **UTF-8** format to prevent any issues with parsing (because I've had them when parsing the JSONs in Haxe)