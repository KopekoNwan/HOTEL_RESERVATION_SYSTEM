migrate((db) => {
  const collection = new Collection({
    "id": "oeyxxgviihyuhu4",
    "created": "2023-05-25 03:41:37.899Z",
    "updated": "2023-05-25 03:41:37.899Z",
    "name": "cancelled_reservation",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "0jkqukh6",
        "name": "cancelled_date",
        "type": "date",
        "required": false,
        "unique": false,
        "options": {
          "min": "",
          "max": ""
        }
      },
      {
        "system": false,
        "id": "fsr0xawb",
        "name": "user",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "_pb_users_auth_",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "username",
            "id"
          ]
        }
      },
      {
        "system": false,
        "id": "ji3a7txy",
        "name": "customer_information",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "v8cua5zxvjxe0mo",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "customer_name",
            "customer_id"
          ]
        }
      },
      {
        "system": false,
        "id": "91g9r9td",
        "name": "room",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "v8cua5zxvjxe0mo",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "room"
          ]
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
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4");

  return dao.deleteCollection(collection);
})
