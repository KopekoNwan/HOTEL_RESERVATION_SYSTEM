migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // remove
  collection.schema.removeField("fsr0xawb")

  // remove
  collection.schema.removeField("ji3a7txy")

  // remove
  collection.schema.removeField("91g9r9td")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // add
  collection.schema.addField(new SchemaField({
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
  }))

  // add
  collection.schema.addField(new SchemaField({
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
      "displayFields": []
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
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
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
})
