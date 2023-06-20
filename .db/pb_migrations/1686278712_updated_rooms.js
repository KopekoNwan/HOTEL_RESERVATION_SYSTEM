migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // remove
  collection.schema.removeField("f1zhs8eh")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "jv9qapf6",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type",
        "price"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "f1zhs8eh",
    "name": "price",
    "type": "number",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null
    }
  }))

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "jv9qapf6",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
