# Pipe pipe_975789b47f17690a21e89b10a702bcbd generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipestringtokenizer import pipe_stringtokenizer
from pipe2py.modules.pipetextinput import pipe_textinput
from pipe2py.modules.pipeitembuilder import pipe_itembuilder
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.piperegex import pipe_regex
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.pipeoutput import pipe_output


def pipe_975789b47f17690a21e89b10a702bcbd(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return [(u'', u'q', u'Status update', u'text', u"Here's #: some #hashtags to play #with")]

    if context and context.describe_dependencies:
        return [u'pipefilter', u'pipeitembuilder', u'pipeloop', u'pipeoutput', u'piperegex', u'piperename', u'pipestringtokenizer', u'pipetextinput']

    forever = pipe_forever()

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_478(context=None, _INPUT=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_stringtokenizer(
            context, _INPUT, conf={'to-str': {'type': 'text', 'value': ' '}})
    
    sw_417 = pipe_textinput(
        context, forever, conf={'debug': {'type': 'text', 'value': ''}, 'default': {'type': 'text', 'value': "Here's #: some #hashtags to play #with"}, 'prompt': {'type': 'text', 'value': 'Status update'}, 'name': {'type': 'text', 'value': 'q'}, 'position': {'type': 'number', 'value': ''}})
    
    sw_424 = pipe_itembuilder(
        context, forever, conf={'attrs': [{'value': {'terminal': 'attrs_1_value', 'type': 'text'}, 'key': {'type': 'text', 'value': 'title'}}]}, attrs_1_value=sw_417)
    
    sw_436 = pipe_filter(
        context, sw_424, conf={'COMBINE': {'type': 'text', 'value': 'and'}, 'MODE': {'type': 'text', 'value': 'permit'}, 'RULE': [{'field': {'type': 'text', 'value': 'title'}, 'value': {'type': 'text', 'value': '#'}, 'op': {'type': 'text', 'value': 'contains'}}]})
    
    sw_447 = pipe_regex(
        context, sw_436, conf={'RULE': [{'field': {'type': 'text', 'value': 'title'}, 'globalmatch': {'type': 'text', 'value': '1'}, 'match': {'type': 'text', 'value': ' [^#]*'}, 'replace': {'type': 'text', 'value': ' '}}, {'field': {'type': 'text', 'value': 'title'}, 'match': {'type': 'text', 'value': '^[^#]*'}, 'replace': {'type': 'text', 'value': ''}}]})
    
    sw_470 = pipe_loop(
        context, sw_447, embed=pipe_sw_478, conf={'assign_part': {'type': 'text', 'value': 'all'}, 'assign_to': {'type': 'text', 'value': 'loop:stringtokenizer'}, 'emit_part': {'type': 'text', 'value': 'all'}, 'mode': {'type': 'text', 'value': 'EMIT'}, 'embed': {'type': 'module', 'value': {'type': 'stringtokenizer', 'id': 'sw-478', 'conf': {'to-str': {'type': 'text', 'value': ' '}}}}, 'with': {'type': 'text', 'value': 'title'}})
    
    sw_490 = pipe_filter(
        context, sw_470, conf={'COMBINE': {'type': 'text', 'value': 'and'}, 'MODE': {'type': 'text', 'value': 'permit'}, 'RULE': [{'field': {'type': 'text', 'value': 'content'}, 'value': {'type': 'text', 'value': '#[\\w]'}, 'op': {'type': 'text', 'value': 'matches'}}]})
    
    sw_501 = pipe_rename(
        context, sw_490, conf={'RULE': [{'field': {'type': 'text', 'value': 'content'}, 'op': {'type': 'text', 'value': 'rename'}, 'newval': {'type': 'text', 'value': 'title'}}]})
    
    _OUTPUT = pipe_output(
        context, sw_501, conf={})
    
    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_975789b47f17690a21e89b10a702bcbd(Context())

    for i in pipeline:
        print i