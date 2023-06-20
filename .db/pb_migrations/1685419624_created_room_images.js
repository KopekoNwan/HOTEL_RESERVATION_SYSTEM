migrate((db) => {
  const collection = new Collection({
    "id": "obbhx5i2333jgko",
    "created": "2023-05-30 04:07:04.129Z",
    "updated": "2023-05-30 04:07:04.129Z",
    "name": "room_images",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "lswlnkpe",
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
  const collection = dao.findCollectionByNameOrId("obbhx5i2333jgko");

  return dao.deleteCollection(collection);
})
