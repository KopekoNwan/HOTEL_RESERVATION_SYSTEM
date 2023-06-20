migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // update
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
      "displayFields": [
        "username"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // update
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
})
