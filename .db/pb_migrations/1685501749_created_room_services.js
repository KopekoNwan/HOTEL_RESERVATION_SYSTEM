migrate((db) => {
  const collection = new Collection({
    "id": "aorvdhb5ik1l8pi",
    "created": "2023-05-31 02:55:49.509Z",
    "updated": "2023-05-31 02:55:49.509Z",
    "name": "room_services",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "fy17khma",
        "name": "service",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
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
  const collection = dao.findCollectionByNameOrId("aorvdhb5ik1l8pi");

  return dao.deleteCollection(collection);
})
