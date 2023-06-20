migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // remove
  collection.schema.removeField("igb8ke5d")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "7y8sshth",
    "name": "user",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "_pb_users_auth_",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "igb8ke5d",
    "name": "user",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // remove
  collection.schema.removeField("7y8sshth")

  return dao.saveCollection(collection)
})
