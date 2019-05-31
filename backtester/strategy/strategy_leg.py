from backtester.option import Type, Direction
from backtester.datahandler import Schema


class StrategyLeg:
    """Strategy Leg data class"""

    def __init__(self, schema, option_type=Type.CALL, direction=Direction.BUY):
        assert isinstance(schema, Schema)
        assert isinstance(option_type, Type)
        assert isinstance(direction, Direction)

        self.schema = schema
        self.type = option_type
        self.direction = direction
        self._entry_filter = self.schema.type == self.type.value
        self._exit_filter = self.schema.type == self.type.value

    @property
    def entry_filter(self):
        """Returns the entry filter"""
        return self._entry_filter

    @entry_filter.setter
    def entry_filter(self, flt):
        """Sets the entry filter"""
        self._entry_filter = (self.schema.type == self.type.value) & flt

    @property
    def exit_filter(self):
        """Returns the exit filter"""
        return self._exit_filter

    @exit_filter.setter
    def exit_filter(self, flt):
        """Sets the exit filter"""
        self._exit_filter = (self.schema.type == self.type.value) & flt

    def __repr__(self):
        return "StrategyLeg(type={}, direction={}, entry_filter={}, exit_filter={})".format(
            self.type, self.direction, self._entry_filter, self._exit_filter)
