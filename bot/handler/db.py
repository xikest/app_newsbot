from google.cloud import firestore
import logging

class FirestoreStorage:
    def __init__(self, collection_name: str, max_buffer_size: int):
        self.db = firestore.Client()  # Firestore 클라이언트 초기화
        self.collection_name = collection_name
        self.max_buffer_size = max_buffer_size

    def _save_contents(self, contents: str, document_id: str = 'app_newsbot_contents'):
        sent_list = list(self._load_contents(document_id))
        sent_list.append(contents)
        
        # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)

        # Firestore에 저장
        self.db.collection(self.collection_name).document(document_id).set({'contents': sent_list})
        logging.info(f"Saved contents to Firestore under document {document_id}.")

    def _load_contents(self, document_id: str = 'app_newsbot_contents'):
        try:
            doc_ref = self.db.collection(self.collection_name).document(document_id)
            doc = doc_ref.get()

            if doc.exists:
                contents = doc.to_dict().get('contents', [])
                logging.info(f"Loaded contents from Firestore: {contents}")
                return contents
            else:
                logging.warning(f"No document found with ID {document_id}. Returning empty list.")
                return []
        except Exception as e:
            logging.error(f"Failed to load contents from Firestore: {e}")
            return []
