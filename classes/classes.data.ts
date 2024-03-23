import {createContentLoader, ContentData} from "vitepress";

function transformMap({src, frontmatter, url}: ContentData) {
    return {
        frontmatter,
        url,
        title: frontmatter.title || src?.match(/^(.+)\n===+$/m)?.[1].trim()
    };
}

declare const data: ReturnType<typeof transformMap>;
export {data}

export default createContentLoader('*/index.md', {
    includeSrc: true,
    transform: (docs) => docs.map(transformMap),
});
