API_IGNORE_WRITE_FIELDS = [
    "owner",
    "phenotype_id",
    "phenotype_version_id",
    "created",
    "updated",
]
API_IGNORE_TEMPLATE_FIELDS = ["versions", "status", "is_deleted", "owner_access"]
PATH_FOR_STORING_FILE_AFTER_UPDATE_PHENOTYPE = "./assets/gen/upload/update/"
PATH_FOR_STORING_FILE_AFTER_CREATE_PHENOTYPE = "./assets/gen/upload/create/"
