migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("j5ljloee")

  // remove
  collection.schema.removeField("ibxxfa35")

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

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "uaql3g46",
    "name": "check_in",
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
    "id": "achv0emh",
    "name": "check_out",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "j5ljloee",
    "name": "check_in",
    "type": "date",
    "required": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ibxxfa35",
    "name": "check_out",
    "type": "date",
    "required": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  // remove
  collection.schema.removeField("aa2yro2q")

  // remove
  collection.schema.removeField("kfxdbbvq")

  // remove
  collection.schema.removeField("uaql3g46")

  // remove
  collection.schema.removeField("achv0emh")

  return dao.saveCollection(collection)
})
