migrate((db) => {
  const collection = new Collection({
    "id": "kwtbcl5p6z5yood",
    "created": "2023-05-31 05:38:23.700Z",
    "updated": "2023-05-31 05:38:23.700Z",
    "name": "standard_room_gallery",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "zk4qcvqu",
        "name": "room_image",
        "type": "file",
        "required": false,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "maxSize": 5242880,
          "mimeTypes": [],
          "thumbs": [],
          "protected": false
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("kwtbcl5p6z5yood");

  return dao.deleteCollection(collection);
})
