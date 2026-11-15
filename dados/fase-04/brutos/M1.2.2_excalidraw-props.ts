export interface ExcalidrawProps {
  className?: string;
  /**
   * Document that owns Excalidraw's mounted DOM.
   *
   * Set only when it differs from the global `document`, such as when code
   * executing in a parent window mounts Excalidraw into an iframe document.
   * The value must remain stable for the editor's lifetime.
   *
   * @default document
   */
  ownerDocument?: Document;
  onChange?: (
    elements: readonly OrderedExcalidrawElement[],
    appState: AppState,
    files: BinaryFiles,
  ) => void;
  onThemeChange?: (theme: Theme | "system") => void;
  /**
   * note: only subscribes if the props.onIncrement is defined on initial render
   */
  onIncrement?: (event: DurableIncrement | EphemeralIncrement) => void;
  initialData?:
    | (() => MaybePromise<ExcalidrawInitialDataState | null>)
    | MaybePromise<ExcalidrawInitialDataState | null>;
  initialState?: ExcalidrawInitialState;
  /**
   * Invoked as soon as the Excalidraw API is available
   * NOTE editor is not yet mounted, and state is not yet initialized
   */
  onExcalidrawAPI?: (api: ExcalidrawImperativeAPI | null) => void;
  /**
   * Invoked once the editor root is mounted.
   */
  onMount?: (payload: ExcalidrawMountPayload) => void;
  /**
   * Invoked when the editor root is unmounted.
   */
  onUnmount?: () => void;
  /**
   * Invoked once the initial scene is loaded.
   */
  onInitialize?: (api: ExcalidrawImperativeAPI) => void;
  isCollaborating?: boolean;
  onPointerUpdate?: (payload: {
    pointer: { x: number; y: number; tool: "pointer" | "laser" };
    button: "down" | "up";
    pointersMap: Gesture["pointers"];
  }) => void;
  onPaste?: (
    data: ClipboardData,
    event: ClipboardEvent | null,
  ) => Promise<boolean> | boolean;
  /**
   * Called when element(s) are duplicated so you can listen or modify as
   * needed.
   *
   * Called when duplicating via mouse-drag, keyboard, paste, library insert
   * etc.
   *
   * Returned elements will be used in place of the next elements
   * (you should return all elements, including deleted, and not mutate
   * the element if changes are made).
   *
   * The duplicates are the elements in `nextElements` which are not in
   * `prevElements` (see also `data.duplicateElements`). When pasting or
   * inserting onto a frame, their `frameId` is already set. To change a
   * duplicate, return a new object with the same `id`. It is shallow-merged
   * into the duplicate (omitted properties are kept), and your changes are
   * part of the duplication itself (same undo entry, same durable increment).
   *
   * To prevent an element from being duplicated, omit its duplicate from the
   * returned array. References to it from the remaining duplicates are
   * cleared, and a bound text isn't duplicated without its container. To
   * prevent the duplication as a whole, return `false`. If no duplicate
   * remains, the duplication is cancelled and the returned elements are
   * ignored (alt-drag then moves the original elements instead).
   */
  onDuplicate?: (
    nextElements: readonly ExcalidrawElement[],
    /** excludes the duplicated elements */
    prevElements: readonly ExcalidrawElement[],
    /** lookups covering just the elements taking part in the duplication */
    data: OnDuplicateData,
  ) => ExcalidrawElement[] | void | false;
  renderTopLeftUI?: (
    isMobile: boolean,
    appState: UIAppState,
  ) => JSX.Element | null;
  renderTopRightUI?: (
    isMobile: boolean,
    appState: UIAppState,
  ) => JSX.Element | null;
  langCode?: Language["code"];
  viewModeEnabled?: boolean;
  /**
   * Whether the editor accepts user input (pointer, keyboard, wheel, touch,
   * clipboard, drag&drop). When `false`, the scene still renders and reacts
   * to programmatic updates (imperative API), but the user cannot affect it
   * in any way. Implies view mode.
   *
   * Pass a config object to keep specific interactions enabled while the
   * editor is otherwise non-interactive (see `InteractionConfig`):
   *
   * ```tsx
   * <Excalidraw interaction={{ enabled: { links: true } }} />
   * ```
   *
   * @default true
   */
  interaction?: boolean | InteractionConfig;
  /**
   * Whether Excalidraw's default UI is rendered — toolbar, default menus,
   * footer controls, sidebars, and canvas popups. Host UI passed through
   * children (including exported components such as `MainMenu` and `Footer`)
   * or render props continues to render, together with any supporting dialogs
   * it opens.
   *
   * Canvas content (elements, text editing surface, frame names, embeds) still
   * renders, and the editor remains interactive unless `interaction` is set to
   * `false`.
   *
   * Pass a config object to keep specific default controls rendered while the
   * rest of the default UI is hidden (see `UIConfig`):
   *
   * ```tsx
   * <Excalidraw ui={{ enabled: { zoom: true } }} />
   * ```
   *
   * NOTE: this is WIP and what default UI is/is not rendered when ui=false
   * may yet change.
   *
   * @default true
   */
  ui?: boolean | UIConfig;
  /**
   * Forces the active editor tool (controlled). While set, user- and
   * API-driven tool switching is ignored — `setActiveTool` refuses with a
   * console warning, non-forced toolbar buttons render disabled — and the
   * editor snaps back if internal flows reset the tool. The forced tool
   * behaves as if locked (see the tool lock / padlock): it doesn't revert to
   * the selection tool after use, and elements drawn with it aren't
   * auto-selected — without mutating `appState.activeTool.locked`, so the
   * user's persisted padlock preference stays untouched. Unset to return
   * tool control to the editor (the current tool stays active).
   *
   * The forced tool must be activatable to take effect: not disabled via
   * `UIOptions.tools`, and — while the editor is non-interactive — allowed
   * via `interaction.enabled.tools`. Otherwise the editor stays on (or, when
   * non-interactive, resets to) the `selection` tool, and the forced tool is
   * applied once it becomes activatable. `image` cannot be forced (its
   * activation opens the file picker).
   */
  activeTool?:
    | { type: Exclude<ToolType, "image"> }
    | { type: "custom"; customType: string };
  zenModeEnabled?: boolean;
  gridModeEnabled?: boolean;
  objectsSnapModeEnabled?: boolean;
  libraryReturnUrl?: string;
  theme?: Theme;
  // @TODO come with better API before v0.18.0
  name?: string;
  renderCustomStats?: (
    elements: readonly NonDeletedExcalidrawElement[],
    appState: UIAppState,
  ) => JSX.Element;
  UIOptions?: Partial<UIOptions>;
  /**
   * dimensions and size constraints for inserted images
   */
  imageOptions?: ImageOptions;
  detectScroll?: boolean;
  handleKeyboardGlobally?: boolean;
  onLibraryChange?: (libraryItems: LibraryItems) => void | Promise<any>;
  autoFocus?: boolean;
  generateIdForFile?: (file: File) => string | Promise<string>;
  generateLinkForSelection?: (id: string, type: "element" | "group") => string;
  onLinkOpen?: (
    element: NonDeletedExcalidrawElement,
    event: CustomEvent<{
      nativeEvent: MouseEvent | React.PointerEvent<HTMLCanvasElement>;
    }>,
  ) => void;
  onPointerDown?: (
    activeTool: AppState["activeTool"],
    pointerDownState: PointerDownState,
  ) => void;
  onPointerUp?: (
    activeTool: AppState["activeTool"],
    pointerDownState: PointerDownState,
  ) => void;
  onScrollChange?: (scrollX: number, scrollY: number, zoom: Zoom) => void;
  onUserFollow?: (payload: OnUserFollowedPayload) => void;
  children?: React.ReactNode;
  validateEmbeddable?:
    | boolean
    | string[]
    | RegExp
    | RegExp[]
    | ((link: string) => boolean | undefined);
  renderEmbeddable?: (
    element: NonDeleted<ExcalidrawEmbeddableElement>,
    appState: AppState,
  ) => JSX.Element | null;
  aiEnabled?: boolean;
  showDeprecatedFonts?: boolean;
  renderScrollbars?: boolean;
  viewportStatusFrame?: ViewportStatusFrame | null;
  /**
   * Rendered inside the UserList "who's here" dropdown (desktop) and inline
   * in the mobile menu's collaborators section, below a divider. Accepts a
   * render function — called with `isMobile` so hosts can render different
   * UI for each surface — in addition to a plain node.
   */
  currentUserControls?:
    | React.ReactNode
    | ((isMobile: boolean) => React.ReactNode);
  /**
   * The user being followed on the canvas, if any. Controlled by the host —
   * the editor never sets it; it emits follow/unfollow intents via
   * `onUserFollow` (prop or imperative API) and renders the followed
   * user's avatar highlight from this value.
   */
  userToFollow?: UserToFollow | null;
  /**
   * Called before exporting to a file.
   *
   * Allows the host app to intercept and delay saving until async operations
   * (e.g., images are loaded) complete.
   *
   * If Promise/AsyncGenerator is returned, a progress toast will be shown
   * until the operation completes. Generator can yield progress updates.
   */
  onExport?: (
    /** type of export. Currently we only call for JSON exports or
     * JSON-embedded PNG (which is also identified as `json` type here)*/
    type: "json",
    data: {
      elements: readonly ExcalidrawElement[];
      appState: AppState;
      files: BinaryFiles;
    },
    options: {
      /** signal that gets aborted if user cancels the export (e.g. closes
       * the native file picker dialog). In that case, you can either
       * return immediately, or throw AbortError.
       */
      signal: AbortSignal;
    },
  ) => MaybePromise<void> | AsyncGenerator<OnExportProgress, void>;
}
