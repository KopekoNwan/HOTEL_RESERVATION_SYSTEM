migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("aa2yro2q")

  // remove
  collection.schema.removeField("kfxdbbvq")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "xos0t19p",
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
        "room_number",
        "room_type"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "aa2yro2q",
    "name": "room_number",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "kfxdbbvq",
    "name": "room_type",
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
  collection.schema.removeField("xos0t19p")

  return dao.saveCollection(collection)
})
