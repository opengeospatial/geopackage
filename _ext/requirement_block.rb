require 'asciidoctor'
require 'asciidoctor/extensions'

class RequirementBlock < Asciidoctor::Extensions::BlockProcessor
  option :contexts, [:paragraph]
  option :content_model, :simple

  def process parent, reader, attributes
    lines = reader.lines
    lines[0] = "*Req {counter:req}:* " + lines[0]

    Asciidoctor::Block.new parent, :quote, :source => lines, :attributes => attributes
  end
end

Asciidoctor::Extensions.register do |document|
  block :requirement, RequirementBlock
end