# README #

# Upload Tool

Utility for uploading fbx assets using a structured folder system and a naming conventions.

1. From dropdown menu select the asset you are working on
2. Browse for fbx and texture files you want to upload
3. Upload

The tool shows the assets from a sqlite database.
It checks for naming conventions and file types allowed, then renames the asset as defined on the uploader utilites and save that asset on path defined in the configuration file.

In the config.json file you can setup:

* File types allowed
* name conventions for textures
* Paths of server, share and content
