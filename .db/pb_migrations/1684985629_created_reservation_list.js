migrate((db) => {
  const collection = new Collection({
    "id": "v8cua5zxvjxe0mo",
    "created": "2023-05-25 03:33:49.335Z",
    "updated": "2023-05-25 03:33:49.335Z",
    "name": "reservation_list",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "p4tmzkdk",
        "name": "user",
        "type": "relation",
        "required": true,
        "unique": false,
        "options": {
          "collectionId": "_pb_users_auth_",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "username"
          ]
        }
      },
      {
        "system": false,
        "id": "gl2nczef",
        "name": "reservation_date",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "1rm9eqlfw2z6co2",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "reservation_date"
          ]
        }
      },
      {
        "system": false,
        "id": "g2mekoqu",
        "name": "customer_id",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "1rm9eqlfw2z6co2",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "id"
          ]
        }
      },
      {
        "system": false,
        "id": "bfavk6uh",
        "name": "customer_name",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "1rm9eqlfw2z6co2",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "last_name",
            "first_name"
          ]
        }
      },
      {
        "system": false,
        "id": "ui2moic5",
        "name": "room",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "x0hmwdlv02zwb5y",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "room_number"
          ]
        }
      },
      {
        "system": false,
        "id": "spjwmqln",
        "name": "guest",
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
        "id": "yjgoqm6h",
        "name": "duration",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "1rm9eqlfw2z6co2",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": [
            "check_in",
            "check_out"
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
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo");

  return dao.deleteCollection(collection);
})
