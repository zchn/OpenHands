from openhands.events.event import Event, ParentEvent


def test_event_parents_property():
    # Test initial state
    event = Event()
    assert event.parents is None

    # Test setting and getting parents
    parent_events = [
        ParentEvent(id=1, method='process_a'),
        ParentEvent(id=2, method='process_b'),
    ]
    event.parents = parent_events

    # Verify parents are set correctly
    assert event.parents is not None
    assert len(event.parents) == 2
    assert event.parents[0].id == 1
    assert event.parents[0].method == 'process_a'
    assert event.parents[1].id == 2
    assert event.parents[1].method == 'process_b'


def test_parent_event_dataclass():
    # Test ParentEvent creation
    parent = ParentEvent(id=1, method='test_method')
    assert parent.id == 1
    assert parent.method == 'test_method'

    # Test equality
    parent2 = ParentEvent(id=1, method='test_method')
    assert parent == parent2

    # Test different values
    parent3 = ParentEvent(id=2, method='other_method')
    assert parent != parent3
