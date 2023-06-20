migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("t4cjilpb")

  // remove
  collection.schema.removeField("pmcljjdc")

  // remove
  collection.schema.removeField("x80iee0f")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qeswn9pl",
    "name": "last_name",
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
    "id": "44hbpiv2",
    "name": "first_name",
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
    "id": "0mfhqbbe",
    "name": "contact_number",
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
    "id": "aufcwoav",
    "name": "email",
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
    "id": "t4cjilpb",
    "name": "customer",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "last_name",
        "first_name"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "pmcljjdc",
    "name": "email",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "email"
      ]
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "x80iee0f",
    "name": "contact_number",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "ouc9mg423fntace",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "contact"
      ]
    }
  }))

  // remove
  collection.schema.removeField("qeswn9pl")

  // remove
  collection.schema.removeField("44hbpiv2")

  // remove
  collection.schema.removeField("0mfhqbbe")

  // remove
  collection.schema.removeField("aufcwoav")

  return dao.saveCollection(collection)
})
