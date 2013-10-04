require 'asciidoctor'
require 'asciidoctor/extensions'

class RequirementBlock < Asciidoctor::Extensions::BlockProcessor
  option :contexts, [:paragraph]
  option :content_model, :simple

  def process parent, reader, attributes
    block = Asciidoctor::Block.new parent, :quote, :source => reader.lines, :attributes => attributes

    doc = parent.document
    requirement_id = doc.counter('requirement')
    block.id = attributes[2] || "_requirement-#{requirement_id}"
    block.title = "#{doc.attributes['requirement-caption'] || 'Requirement'} #{requirement_id}"

    block
  end
end

Asciidoctor::Extensions.register do |document|
  block :requirement, RequirementBlock
end