import paddleocr
from difflib import SequenceMatcher
import bot.base.log as logger

log = logger.get_logger(__name__)

OCR_JP = paddleocr.PaddleOCR(lang="japan", show_log=False, use_angle_cls=False)
OCR_CH = paddleocr.PaddleOCR(lang="ch", show_log=False, use_angle_cls=False)


# ocr 文字识别图片
def ocr(img, lang="ch"):
    if lang == "ch":
        return OCR_CH.ocr(img, cls=False)
    if lang == "japan":
        return OCR_JP.ocr(img, cls=False)


# ocr_line 文字识别图片，返回所有出现的文字
def ocr_line(img, lang="ch"):
    ocr_result = ocr(img, lang)
    text = ""
    ocr_result = ocr_result[0]
    for text_info in ocr_result:
        if len(text_info) > 0:
            text += text_info[1][0]
    return text


# find_text_pos 查找目标文字在图片中的位置
def find_text_pos(ocr_result, target):
    threshold = 0.6
    result = None
    for text_info in ocr_result:
        if len(text_info) > 0:
            s = SequenceMatcher(None, target, text_info[0][1][0])
            if s.ratio() > threshold:
                result = text_info[0]
                threshold = s.ratio()
    return result


def find_similar_text(target_text, ref_text_list, threshold=0):
    result = ""
    for ref_text in ref_text_list:
        s = SequenceMatcher(None, target_text, ref_text)
        if s.ratio() > threshold:
            result = ref_text
            threshold = s.ratio()
    return result
