from typing import Union, Any

import pywikibot

from config import *
from pywikibot_extension import MyDataSite
from tools import *


class BasePropertyProcessor:
    def __init__(self, repo, debug, column, row_new_fields, claim_direct_from_wd, property_for_new_field, item_new_field):
        self.property_for_new_field: Union[str, None] = property_for_new_field
        self.item_new_field: Union[pywikibot.ItemPage, None] = item_new_field
        self.debug: bool = debug
        self.column: Union[str, None] = column
        self.row_new_fields: dict = row_new_fields
        self.repo: Union[MyDataSite, None] = repo
        self.claim_direct_from_wd = claim_direct_from_wd

    def set_claim_direct_from_wd(self, claim_direct_from_wd):
        self.claim_direct_from_wd = claim_direct_from_wd

    def set_repo(self, repo: MyDataSite):
        self.repo = repo

    def set_row_new_fields(self, row_new_fields: dict):
        self.row_new_fields = row_new_fields

    def set_column(self, column: str):
        self.column = column

    def set_debug(self, debug: bool):
        self.debug = debug

    def set_item_new_field(self, item_new_field: pywikibot.ItemPage):
        self.item_new_field = item_new_field

    def set_property_for_new_field(self, property_for_new_field: str):
        self.property_for_new_field = property_for_new_field

    def get_qid_claims_direct_from_wd(self) -> list:
        qid_claims_direct_from_wd = []
        for cdfwd in self.claim_direct_from_wd:
            if type(cdfwd) is pywikibot.ItemPage:
                qid_claims_direct_from_wd.append(cdfwd.getID())
        return qid_claims_direct_from_wd


class PropertyProcessor374a(BasePropertyProcessor):
    QID_OCCUPATION = 'Q12737077'

    def process(self):
        class_occupation = pywikibot.ItemPage(self.repo, PropertyProcessor374a.QID_OCCUPATION)
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_occupation = pywikibot.ItemPage(self.repo, item_in_list)

            if item_occupation.getID() not in qid_claims_direct_from_wd and item_occupation.getID() not in Config.occupations_not_used_in_occupation_because_is_in_function:
                # ocupp_qid = item_occupation.getID()
                if is_item_subclass_of(item_occupation, class_occupation):
                    if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                        add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                              item_occupation,
                                              self.row_new_fields['_id'])

class PropertyProcessor370a(BasePropertyProcessor):

    def process(self):
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_place = pywikibot.ItemPage(self.repo, item_in_list)

            if item_place.getID() not in qid_claims_direct_from_wd:
                if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                    add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                          item_place,
                                          self.row_new_fields['_id'])

class PropertyProcessor370b(BasePropertyProcessor):

    def process(self):
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_place = pywikibot.ItemPage(self.repo, item_in_list)

            if item_place.getID() not in qid_claims_direct_from_wd:
                if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                    add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                          item_place,
                                          self.row_new_fields['_id'])

class PropertyProcessor370f(BasePropertyProcessor):

    def process(self):
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_place = pywikibot.ItemPage(self.repo, item_in_list)

            if item_place.getID() not in qid_claims_direct_from_wd:
                if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                    add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                          item_place,
                                          self.row_new_fields['_id'])

class PropertyProcessor372a(BasePropertyProcessor):

    def set_datas_from_wd(self, datas_from_wd: dict[str, Any]):
        self.datas_from_wd = datas_from_wd

    def process(self):
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_occupation = pywikibot.ItemPage(self.repo, item_in_list)

            if item_occupation.getID() not in qid_claims_direct_from_wd and item_occupation.getID() not in Config.fields_of_work_not_used_in_field_of_work_because_is_not_ok:
                # ocupp_qid = item_occupation.getID()
                occupations_direct_from_wd = get_claim_from_item_by_property(self.datas_from_wd,
                                                                             Config.property_occupation)  # pro kontrolu
                qid_occupations_claims_direct_from_wd = []
                for odfwd in occupations_direct_from_wd:
                    if type(odfwd) is pywikibot.ItemPage:
                        qid_occupations_claims_direct_from_wd.append(odfwd.getID())
                if item_occupation.getID() not in qid_occupations_claims_direct_from_wd:
                    if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                        add_new_field_to_item(self.debug, self.repo, self.item_new_field,
                                              self.property_for_new_field,
                                              item_occupation,
                                              self.row_new_fields['_id'])


class PropertyProcessorOne(BasePropertyProcessor):
    def process(self):
        if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
            add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                  self.row_new_fields[self.column],
                                  self.row_new_fields['_id'])

class PropertyProcessor377a(BasePropertyProcessor):

    def process(self):
        qid_claims_direct_from_wd = self.get_qid_claims_direct_from_wd()
        for item_in_list in self.row_new_fields[self.column]:
            item_language = pywikibot.ItemPage(self.repo, item_in_list)

            if item_language.getID() not in qid_claims_direct_from_wd:
                if self.row_new_fields[self.column] not in self.claim_direct_from_wd:
                    add_new_field_to_item(self.debug, self.repo, self.item_new_field, self.property_for_new_field,
                                          item_language,
                                          self.row_new_fields['_id'])