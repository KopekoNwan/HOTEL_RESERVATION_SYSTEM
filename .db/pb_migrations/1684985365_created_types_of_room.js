migrate((db) => {
  const collection = new Collection({
    "id": "kigjd431nqoyf61",
    "created": "2023-05-25 03:29:25.785Z",
    "updated": "2023-05-25 03:29:25.785Z",
    "name": "types_of_room",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "4jzd5iys",
        "name": "type",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "rftxsn0w",
        "name": "price",
        "type": "number",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null
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
  const collection = dao.findCollectionByNameOrId("kigjd431nqoyf61");

  return dao.deleteCollection(collection);
})
