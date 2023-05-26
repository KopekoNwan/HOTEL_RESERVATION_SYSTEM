migrate((db) => {
  const collection = new Collection({
    "id": "x0hmwdlv02zwb5y",
    "created": "2023-05-25 03:28:17.371Z",
    "updated": "2023-05-25 03:28:17.371Z",
    "name": "rooms",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "i47iy8tx",
        "name": "room_number",
        "type": "number",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null
        }
      },
      {
        "system": false,
        "id": "rb0l9k8q",
        "name": "status",
        "type": "bool",
        "required": false,
        "unique": false,
        "options": {}
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
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y");

  return dao.deleteCollection(collection);
})
