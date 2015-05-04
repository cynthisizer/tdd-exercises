require_relative 'calculator'
require 'test/unit'



class CalculatorTest < Test::Unit::TestCase


  @@cal = Calculator.new


  def test_return_string()

    assert_equal('S', @@cal.calculate('S'), 'Expected: S, got ' + @@cal.calculate('S'))

  end




end