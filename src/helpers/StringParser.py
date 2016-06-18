class StringParser:
    @staticmethod
    def between(data, str_before, str_after) -> str:
        # Find and validate before-part.
        pos_a = data.find(str_before)
        if pos_a == -1:
            return ""
        # Find and validate after part.
        pos_b = data.find(str_after)
        if pos_b == -1:
            return ""
        # Return middle part.
        adjusted_pos_a = pos_a + len(str_before)
        if adjusted_pos_a >= pos_b:
            return ""
        value = data[adjusted_pos_a:pos_b]
        return str.strip(value)

    @staticmethod
    def before(data, before):
        # Find first part and return slice before it.
        pos_a = data.find(before)
        if pos_a == -1:
            return ""
        return data[0:pos_a]

    @staticmethod
    def after(data, after):
        # Find and validate first part.
        pos_a = data.rfind(after)
        if pos_a == -1:
            return ""
        # Returns chars after the found string.
        adjusted_pos_a = pos_a + len(after)
        if adjusted_pos_a >= len(data):
            return ""
        return data[adjusted_pos_a:]