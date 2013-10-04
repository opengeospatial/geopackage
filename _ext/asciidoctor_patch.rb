#
# Asciidoctor monkey patch to get the section numbering we want for the appendices.
#

require 'asciidoctor'
require 'asciidoctor/backends/html5'

module Asciidoctor
  class Section
    def sectnum(delimiter = '.', append = nil)
      append ||= (append == false ? '' : delimiter)

      if !@level.nil? && @level > 1 && @parent.is_a?(Section)
        if @parent.appendix_number
          "#{@parent.appendix_number}#{delimiter}#{@number}#{append}"
        else
          "#{@parent.sectnum(delimiter)}#{@number}#{append}"
        end
      else
        if appendix_number
          ""
        else
          "#{@number}#{append}"
        end

      end
    end

    def appendix_number
      entry = Array === attributes[:attribute_entries] && attributes[:attribute_entries].find { |entry| entry.name == 'appendix-number' }
      entry ? entry.value : nil
    end
  end
end